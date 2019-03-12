"""
CVEItem class.
"""


import json


class CVEItem:
    """
    CVEItem class.

    Used for parsing data from CVE Files
    """

    def __init__(self, cve_item: dict):
        cve = cve_item.get('cve', {})

        self.id = cve.get('CVE_data_meta', {}).get('ID', None)
        self.vendors = []
        self.cwes = []
        self.references = []
        self.descriptions = []
        self.cpes = []
        self.impact = cve_item.get('impact', {})
        self.published_date = cve_item.get('publishedDate', None)
        self.last_modified_date = cve_item.get('lastModifiedDate', None)

        # Vendors: vendor name, product name, product versions
        vendor_data = cve.get('affects', {}).get('vendor', {}).get('vendor_data', [])
        for vendor in vendor_data:
            products = []

            product_data = vendor.get('product', {}).get('product_data', [])
            for product in product_data:
                versions = []

                version_data = product.get('version', {}).get('version_data', [])
                for version in version_data:
                    versions.append(version.get('version_value', None))

                products.append(
                    {
                        'product': product.get('product_name', None),
                        'versions': versions
                    }
                )

            self.vendors.append(
                json.dumps(
                    {
                        'vendor': vendor.get('vendor_name', None),
                        'products': products
                    }
                )
            )

        del vendor_data

        # CWEs
        problemtype_data = cve.get('problemtype', {}).get('problemtype_data', [])
        for problemtype in problemtype_data:
            description = problemtype.get('description', [])

            for d in description:
                self.cwes.append(d.get('value', None))

        del problemtype_data

        # References
        reference_data = cve.get('references', {}).get('reference_data', [])
        for ref in reference_data:
            self.references.append(ref.get('url', None))

        del reference_data

        # Descriptions
        description_data = cve.get('description', {}).get('description_data', [])
        for description in description_data:
            self.descriptions.append(description.get('value', None))

        del cve
        del description_data

        # CPEs
        configurations = cve_item.get('configurations', {})
        nodes = configurations.get('nodes', [])
        for node in nodes:
            cpe_match = node.get('cpe_match', [])

            for cpe in cpe_match:
                self.cpes.append(cpe.get('cpe23Uri', None))

        del configurations
        del nodes

    def to_dict(self):
        return {
            'cve_id': self.id,
            'vendors': self.vendors,
            'cwes': self.cwes,
            'references': self.references,
            'descriptions': self.descriptions,
            'cpes': self.cpes,
            'impact': json.dumps(self.impact),
            'published_date': self.published_date,
            'last_modified_date': self.last_modified_date
        }
