# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SIF_SCHEME(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from sif_app.my_sif.doctype.sif_fund_manager_child.sif_fund_manager_child import SIF_FundManagerChild
		from sif_app.my_sif.doctype.sif_plan.sif_plan import SIF_Plan

		amc: DF.Link | None
		category: DF.Data
		exit_load: DF.Text | None
		face_value: DF.Data | None
		fund_managers: DF.Table[SIF_FundManagerChild]
		fund_name: DF.Data
		investment_strategy: DF.SmallText | None
		minimum_additional_amount: DF.SmallText | None
		minimum_application_amount: DF.SmallText | None
		minimum_redemption_amount: DF.SmallText | None
		plans: DF.Table[SIF_Plan]
		potential_risk_class: DF.Data | None
		sebi_code: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "SIF_SCHEME"
