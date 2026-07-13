# Copyright (c) 2026, Satyam Raj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SchemeDetail(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		additional_investment: DF.Currency
		benchmark: DF.Data | None
		category: DF.Data | None
		exit_load: DF.SmallText | None
		expense_ratio: DF.Percent
		fund_size: DF.Currency
		investment_objective: DF.LongText | None
		investment_strategy: DF.LongText | None
		lock_in_period: DF.Data | None
		minimum_investment: DF.Currency
		minimum_sip: DF.Currency
		name: DF.Int | None
		risk_level: DF.Literal["Low", "Moderate", "Moderately High", "High", "Very High"]
		sif: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Scheme Detail"
