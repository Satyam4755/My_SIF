# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FundManager(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		biography: DF.LongText | None
		experience: DF.Int
		image: DF.AttachImage | None
		manager_name: DF.Data | None
		name: DF.Int | None
		qualification: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Fund Manager"
