import xml.etree.ElementTree as ET
import xmlschema
from typing import Dict, Any, Optional
import yaml
from pathlib import Path


def parse_xml_to_dict(root: ET.Element) -> Dict[str, Any]:
    """
    Parses an XML element and its children into a dictionary.

    Args:
        root (ET.Element): The root XML element to parse.

    Returns:
        Dict[str, Any]: A dictionary representation of the XML element and its children.
    """
    result_dict = {}
    for child in root:
        job_type = child.tag.split("}")[1]
        result_dict["job_type"] = job_type
        for sub_child in child:
            key = sub_child.tag.split("}")[1]
            try:
                value = (
                    float(sub_child.text)
                    if "." in sub_child.text
                    else int(sub_child.text)
                )
            except (ValueError, TypeError):
                value = sub_child.text
            result_dict[key] = value
    return result_dict


def import_and_validate_xml(
    xml_file_path: Path, xsd_file_path: Optional[Path] = None
) -> Dict:
    """
    Parses an XML file and optionally validates it against an XSD schema.

    Args:
        xml_file_path (Path): The path to the XML file.
        xsd_file_path (Optional[str]): The path to the XSD file for validation (optional).

    Returns:
        root (ET.Element): The root XML element to parse.

    Raises:
        ET.ParseError: If there is an error parsing the XML file.
        xmlschema.exceptions.XMLSchemaError: If there is an error validating the XML file against the schema.
        ValueError: If the XML file is not valid according to the specified schema.
    """
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        if xsd_file_path:
            schema = xmlschema.XMLSchema(xsd_file_path)
            if not schema.is_valid(tree):
                raise ValueError(
                    "XML file is not valid according to the specified schema."
                )
            return root
    except ET.ParseError as e:
        raise ET.ParseError(f"Error parsing XML: {str(e)}") from e
    except xmlschema.exceptions.XMLSchemaError as e:
        raise xmlschema.exceptions.XMLSchemaError(
            f"Error validating XML against schema: {str(e)}"
        ) from e


def read_yaml(file_path: Path) -> Dict[str, Any]:
    """
    Reads a YAML configuration file and returns its contents as a dictionary.

    Args:
        file_path (Path): The path to the YAML file.

    Returns:
        Dict[str, Any]: A dictionary representing the parsed YAML file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} was not found.") from e
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file: {e}") from e


if __name__ == "__main__":
    xml_file_path = "build_list.xml"
    xsd_file_path = "job_schema.xsd"

    root_dict = import_and_validate_xml(xml_file_path, xsd_file_path)
    print(root_dict)
