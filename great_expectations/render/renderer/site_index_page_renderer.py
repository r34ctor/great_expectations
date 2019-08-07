from collections import OrderedDict
from .renderer import Renderer

class SiteIndexPageRenderer(Renderer):

    @classmethod
    def render(cls, index_links_dict):

        sections = []

        for source, generators in index_links_dict.items():
            content_blocks = []

            source_header_block = {
                "content_block_type": "header",
                "header": source,
                "styling": {
                    "classes": ["col-12"],
                    "header": {
                        "classes": ["alert", "alert-secondary"]
                    }
                }
            }
            content_blocks.append(source_header_block)

            for generator, data_assets in generators.items():
                generator_header_block = {
                    "content_block_type": "header",
                    "header": generator,
                    "styling": {
                        "classes": ["col-12", "ml-4"],
                    }
                }
                content_blocks.append(generator_header_block)

                horizontal_rule = {
                    "content_block_type": "string_template",
                    "string_template": {
                        "template": "",
                        "params": {},
                        "tag": "hr"
                    },
                    "styling": {
                        "classes": ["col-12"],
                    }
                }
                content_blocks.append(horizontal_rule)

                for data_asset, link_lists in data_assets.items():
                    data_asset_heading = {
                        "content_block_type": "string_template",
                        "string_template": {
                            "template": "$data_asset",
                            "params": {
                                "data_asset": data_asset
                            },
                            "tag": "blockquote",
                            "styling": {
                                "params": {
                                    "data_asset": {
                                        "classes": ["blockquote"],
                                    }
                                }
                            }
                        },
                        "styling": {
                            "classes": ["col-sm-4", "col-xs-12", "pl-sm-5", "pl-xs-0"],
                            "styles": {
                                "margin-top": "10px",
                                "word-break": "break-all"
                            }
                        }
                    }
                    content_blocks.append(data_asset_heading)

                    expectation_suite_links = link_lists["expectation_suite_links"]
                    expectation_suite_link_table_rows = [
                        [{
                            "content_block_type": "string_template",
                            "string_template": {
                                "template": "$link_text",
                                "params": {
                                    "link_text": link_dict["expectation_suite_name"]
                                },
                                "tag": "a",
                                "styling": {
                                    "attributes": {
                                        "href": link_dict["filepath"]
                                    }
                                }
                            }
                        }] for link_dict in expectation_suite_links
                    ]
                    expectation_suite_link_table = {
                        "content_block_type": "table",
                        "subheader": "Expectation Suites",
                        "table": expectation_suite_link_table_rows,
                        "styling": {
                            "classes": ["col-sm-4", "col-xs-12"],
                            "styles": {
                                "margin-top": "10px"
                            },
                            "body": {
                                "classes": ["table", "table-sm", ],
                            }
                        },
                    }
                    content_blocks.append(expectation_suite_link_table)

                    validation_links = link_lists["validation_links"]
                    validation_link_table_rows = [
                        [{
                            "content_block_type": "string_template",
                            "string_template": {
                                "template": "$link_text",
                                "params": {
                                    "link_text": (link_dict["run_id"] + "-" + link_dict[
                                        "expectation_suite_name"] + "-ProfilingResults") if "ProfilingResults" in link_dict[
                                        "filepath"] else
                                    (link_dict["run_id"] + "-" + link_dict["expectation_suite_name"] + "-ValidationResults")
                                },
                                "tag": "a",
                                "styling": {
                                    "attributes": {
                                        "href": link_dict["filepath"]
                                    }
                                }
                            }
                        }] for link_dict in validation_links
                    ]
                    validation_link_table = {
                        "content_block_type": "table",
                        "subheader": "Batch Validations",
                        "table": validation_link_table_rows,
                        "styling": {
                            "classes": ["col-sm-4", "col-xs-12"],
                            "styles": {
                                "margin-top": "10px"
                            },
                            "body": {
                                "classes": ["table", "table-sm", ],
                            }
                        },
                    }
                    content_blocks.append(validation_link_table)

            section = {
                "section_name": source,
                "content_blocks": content_blocks
            }
            sections.append(section)

        return sections
