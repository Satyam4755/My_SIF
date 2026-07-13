# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SectorAllocation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		name: DF.Int | None
		percentage: DF.Percent
		sector_name: DF.Data | None
		sif: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Sector Allocation"
