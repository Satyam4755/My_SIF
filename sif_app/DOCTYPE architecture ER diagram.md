for confirmation


```mermaid
erDiagram
    
    Details ||--o{ AMC : linked_with
    Details ||--o{ subcategory_name : linked_with
    PLAN ||--o{ SIF_SCHEME : linked_with
    PLAN ||--o{ PERFORMANCE : linked_with
    PERFORMANCE ||--o{ PLAN : linked_with
    SIF_SCHEME ||--o{ Details : Tab1
    SIF_SCHEME ||--o{ Scheme_Allocation : Tab2
    SIF_SCHEME ||--o{ Scheme_Fund_manager : Tab3
    SIF_SCHEME ||--o{ Documents : Tab4
    Scheme_Fund_manager ||--o{ FUND_MANAGER_CHILD : has
    FUND_MANAGER ||--o{ FUND_MANAGER_CHILD : assigned_to

    Scheme_Allocation ||--o{ Scheme_Allocation_CHILD : has


    AMC {
        Data registration_number PK
        Data sif_name 
        Data amc_name 
        Select RTA 
        Check is_active 
        Data amc_code 

    }

    FUND_MANAGER {
        Data manager_name
    }

    FUND_MANAGER_CHILD {
        Link manager_name FK
        Date from_date 
        Date to_date 
        Check is_active 
    }

    SIF_SCHEME {
        Tab1 Details
        Tab2 Scheme_allocation
        Tab3 Fund_manager
        Tab4 Documents
    }

    Details{
        Data scheme_name
        Link AMC
        Data sebi_code 
        Check is_active
        Check is_active_for_subs.
        Date nfo_start_date
        Date nfo_end_date
        Date nfo_allotment_date
        Date scheme_reopen_date
        Select scheme_type
        Select investment_strategy
        Link scheme_subcategory
        Int risk_band
        Currency minimum_subscription
        Long_text scheme_objective
        Small_text exit_load
    }

    Scheme_Allocation{
        Table allocations
    }


    Scheme_Fund_manager{
        Table fund_manager
    }

    Documents{
        Data isid_url
        Data kim_url
        Data sai_url
        Data factsheet_url
        Data monthly_portfolio_disclosure_url
    }

    subcategory_name{
        Data subcategory_name PK
    }

    PLAN {
        Fiend_type name e.g_value/keys
        Data isin PK
        Link scheme
        Data full_name plan_name
        Select type Regular
        Select option IDCW
        Select sub_option Payout
        Select period Weekly
        FLoat nav 10
        Date nav_date 17-07-2026
        link performance
        Data sif_code SIF-12
        Data rta_code B01
    }

    Scheme_Allocation_CHILD{
        Small_Text allocation_type
        Percent minimum_allocation_percentage
        Percent maximum_allocation_percentage
    }

    PERFORMANCE {
        Link scheme_plan PK
        Data title
        Date performance_date

        Percent return_1_day
        Percent return_1_week
        Percent return_1_month
        Percent return_3_month
        Percent return_6_month
        Percent return_1_year
        Percent return_2_year
        Percent return_3_year
        Percent return_5_year
        Percent return_7_year
        Percent return_10_year
        Percent since_inception

        Datetime last_updated
    }
```
