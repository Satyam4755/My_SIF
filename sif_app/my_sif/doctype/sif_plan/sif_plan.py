# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SIF_Plan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amfi_code: DF.Data | None
		isin_code: DF.Data | None
		mode: DF.Literal["Regular", "Direct"]
		option: DF.Literal["Growth", "IDCW Payout", "IDCW Reinvestment", "IDCW Transfer"]
		plan_name: DF.Data
		rta_code: DF.Data | None
		sif_code: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "SIF_Plan"
