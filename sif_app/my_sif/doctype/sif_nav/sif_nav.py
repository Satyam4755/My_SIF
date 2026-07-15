# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SIF_NAV(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from sif_app.my_sif.doctype.sif_plan.sif_plan import SIF_Plan

		nav: DF.Float
		nav_date: DF.Date
		plan: DF.Table[SIF_Plan]
		sif_code: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "SIF_NAV"
