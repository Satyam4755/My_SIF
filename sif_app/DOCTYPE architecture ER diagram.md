for confirmation


```mermaid
erDiagram

    AMC ||--o{ Details : manages
    
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
        Data subcategory_name
    }

    PLAN {
        Data isin PK
        Link scheme
        Data full_name
        Select type
        Select option
        Select sub_option
        Select period
        FLoat nav
        Date nav_date
        link performance
        Data sif_code
        Data rta_code
    }

    PERFORMANCE {
        Link scheme_plan
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
