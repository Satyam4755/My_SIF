# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SIF_PERFORMANCE(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		plan: DF.Link | None
		return_10_year: DF.Float
		return_1_day: DF.Float
		return_1_month: DF.Float
		return_1_week: DF.Float
		return_1_year: DF.Float
		return_2_year: DF.Float
		return_3_month: DF.Float
		return_3_year: DF.Float
		return_5_year: DF.Float
		return_6_month: DF.Float
		return_7_year: DF.Float
		sif_code: DF.Data
		since_launch: DF.Float
	# end: auto-generated types

	_DOCTYPE_NAME = "SIF_PERFORMANCE"
