for confirmation

```mermaid
erDiagram

    AMC ||--o{ SIF_SCHEME : manages
    SIF_SCHEME ||--o{ FUND_MANAGER_CHILD : has
    FUND_MANAGER ||--o{ FUND_MANAGER_CHILD : assigned_to

    SIF_SCHEME ||--o{ PLAN : contains
    PLAN ||--o{ NAV : has
    PLAN ||--|| PERFORMANCE : has


    AMC {
        Data name PK
        Data amc_code
        Data amc_name
    }

    FUND_MANAGER {
        Data name PK
        Data manager_name
    }

    FUND_MANAGER_CHILD {
        Link fund_manager

        Data manager_type
        Date from_date
    }

    SIF_SCHEME {
        Data name PK

        Data sebi_code UNIQUE

        Data fund_name
        Text investment_strategy
        Data category
        Data potential_risk_class

        Data face_value

        Data minimum_application_amount
        Data minimum_additional_amount
        Data minimum_redemption_amount

        Text exit_load

        Link amc

        Datetime last_updated
    }

    PLAN {
        Data mode
        Data option
        Data plan_name

        Data sif_code
        Data amfi_code
        Data isin_code
        Data rta_code
    }

    NAV {
        Link plan

        Date nav_date
        Float nav
    }

    PERFORMANCE {
        Link plan

        Float return_1_day
        Float return_1_week
        Float return_1_month
        Float return_3_month
        Float return_6_month
        Float return_1_year
        Float return_2_year
        Float return_3_year
        Float return_5_year
        Float return_7_year
        Float return_10_year
        Float since_launch

        Datetime last_updated
    }
```