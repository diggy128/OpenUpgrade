# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
<<<<<<< Updated upstream
#    This migration script copyright (C) 2010-2014 Akretion
=======
#    This module copyright (C) 2017 Dimitrios Tanis (jtanis@tanisfood.gr)
>>>>>>> Stashed changes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes
from openerp.openupgrade import openupgrade


@openupgrade.migrate()
def migrate(cr, version):
<<<<<<< Updated upstream
    execute = openupgrade.logged_query
    execute(cr, "UPDATE hr_applicant SET response = NULL WHERE response = 0")
=======
    cr.execute(
        "UPDATE hr_applicant SET response = NULL WHERE response = 0;"
    )
>>>>>>> Stashed changes
