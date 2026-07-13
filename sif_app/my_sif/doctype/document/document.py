# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Document(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		document: DF.Attach | None
		document_type: DF.Literal["SID", "KIM", "Factsheet", "Presentation", "Other"]
		name: DF.Int | None
		sif: DF.Link | None
		uploaded_date: DF.Date | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Document"
