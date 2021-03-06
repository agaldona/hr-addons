# -*- coding: utf-8 -*-
# (c) 2016 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "HR Contract History",
    'version': '8.0.1.2.0',
    'license': "AGPL-3",
    'author': "AvanzOSC",
    'website': "http://www.avanzosc.es",
    'contributors': [
        "Ana Juaristi <anajuaristi@avanzosc.es>",
        "Alfredo de la Fuente <alfredodelafuente@avanzosc.es",
    ],
    "category": "Human Resources",
    "depends": [
        'hr_contract',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/hr_contract_view.xml',
    ],
    "installable": True,
}
