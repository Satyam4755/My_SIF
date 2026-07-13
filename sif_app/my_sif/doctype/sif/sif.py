# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SIF(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amc_name: DF.Data | None
		benchmark: DF.Data | None
		category: DF.Data | None
		description: DF.SmallText | None
		fund_manager: DF.Link | None
		launch_date: DF.Date | None
		name: DF.Int | None
		performance: DF.Link | None
		scheme_detail: DF.Link | None
		scheme_name: DF.Data | None
		sif_code: DF.Data | None
		status: DF.Literal["Active", "Closed"]
	# end: auto-generated types

	_DOCTYPE_NAME = "SIF"
