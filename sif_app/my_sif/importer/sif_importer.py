import frappe
from sif_app.my_sif.services.github_service import GitHubService

@frappe.whitelist()
def import_sif_master():
    """
    Imports SIF Master data from GitHub JSON files inside scheme/details/.
    """
    logger = frappe.logger("sif_importer")
    logger.info("Starting SIF Master Import from scheme/details/ JSONs...")
    
    try:
        service = GitHubService()
        
        # 1. List every JSON file inside data/sif/scheme/details/
        details_dir = "scheme/details"
        files = service.list_directory(details_dir)
        
        if not files:
            logger.error(f"No files found in {details_dir} or failed to fetch directory.")
            return {
                "success": False,
                "created": 0,
                "updated": 0,
                "failed": 0,
                "error": "No files found or API rate limit exceeded."
            }
            
        json_files = [f for f in files if f.endswith('.json')]
        
        created = 0
        updated = 0
        failed = 0
        
        # 2. For each JSON file
        for filename in json_files:
            try:
                relative_path = f"{details_dir}/{filename}"
                # Download it
                json_data = service.get_json(relative_path)
                
                if not json_data or not isinstance(json_data, dict):
                    logger.warning(f"Skipping {filename}: Invalid or empty JSON data.")
                    failed += 1
                    continue
                    
                # 3. Extract master information
                # Map JSON fields to: SIF Code, Scheme Name, AMC, Category, Benchmark, Launch Date, Status, Description
                
                # Derive SIF code from JSON or fallback to filename (e.g. s_13.json -> s_13)
                sif_code = json_data.get("sif_code") or json_data.get("sebi_code") or filename.replace('.json', '')
                
                scheme_name = json_data.get("scheme_name") or json_data.get("fund_name") or json_data.get("name")
                amc_name = json_data.get("amc_name") or json_data.get("amc") or json_data.get("fund_house")
                category = json_data.get("category") or json_data.get("scheme_category")
                benchmark = json_data.get("benchmark") or json_data.get("index_name") or ""
                
                # Parse launch date safely
                raw_date = json_data.get("launch_date") or json_data.get("allotment_date")
                launch_date = None
                if raw_date:
                    if "T" in str(raw_date):
                        launch_date = str(raw_date).split("T")[0]
                    else:
                        launch_date = str(raw_date)
                        
                status = json_data.get("status") or json_data.get("fund_type")
                description = json_data.get("description") or json_data.get("objective") or json_data.get("scheme_objective")
                
                # Handle possible nulls to prevent Frappe validation errors
                scheme_name = scheme_name or ""
                amc_name = amc_name or ""
                category = category or ""
                status = status or ""
                description = description or ""

                # 4. Create or update SIF DocType
                existing_name = frappe.db.exists("SIF", {"sif_code": sif_code})
                
                if existing_name:
                    # Update
                    doc = frappe.get_doc("SIF", existing_name)
                    doc.scheme_name = scheme_name
                    doc.amc_name = amc_name
                    doc.category = category
                    doc.benchmark = benchmark
                    if launch_date:
                        doc.launch_date = launch_date
                    doc.status = status
                    doc.description = description
                    
                    doc.save()
                    updated += 1
                else:
                    # Create
                    doc = frappe.get_doc({
                        "doctype": "SIF",
                        "sif_code": sif_code,
                        "scheme_name": scheme_name,
                        "amc_name": amc_name,
                        "category": category,
                        "benchmark": benchmark,
                        "launch_date": launch_date,
                        "status": status,
                        "description": description
                    })
                    
                    doc.insert()
                    created += 1
                    
            except Exception as e:
                logger.error(f"Failed to import SIF from {filename}: {str(e)}")
                failed += 1
                
        # 5. Commit only once after the entire import
        frappe.db.commit()
        
        logger.info(f"SIF Master Import Complete: {created} created, {updated} updated, {failed} failed.")
        return {
            "success": True,
            "created": created,
            "updated": updated,
            "failed": failed
        }
        
    except Exception as e:
        logger.error(f"Fatal error during SIF master import: {str(e)}")
        return {
            "success": False,
            "created": 0,
            "updated": 0,
            "failed": 0,
            "error": str(e)
        }
