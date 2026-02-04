import sys
import glob
from rdflib import Graph
from pyshacl import validate

def validate_ontology():
    # Load the core ontology and shapes
    ontology_file = "beast_mode_ontology.ttl"
    shapes_graph = Graph()
    try:
        shapes_graph.parse(ontology_file, format="turtle")
        print(f"Loaded core ontology: {ontology_file}")
    except Exception as e:
        print(f"Error loading core ontology {ontology_file}: {e}")
        return False

    # Find all TTL files to validate
    ttl_files = glob.glob("**/*.ttl", recursive=True)
    all_valid = True

    for file_path in ttl_files:
        # Skip the core ontology itself when validating "data" against it,
        # although generally self-validation is fine, we want to check instances mostly.
        # But we should check if it parses at least.
        
        print(f"Validating {file_path}...")
        
        data_graph = Graph()
        try:
            data_graph.parse(file_path, format="turtle")
        except Exception as e:
            print(f"  Syntax Error in {file_path}: {e}")
            all_valid = False
            continue

        # Run SHACL validation
        # We use the core ontology as the shapes graph
        conforms, results_graph, results_text = validate(
            data_graph,
            shacl_graph=shapes_graph,
            ont_graph=None,
            inference='rdfs',
            abort_on_first=False,
            allow_infos=False,
            allow_warnings=False,
            meta_shacl=False,
            advanced=True,
            js=False,
            debug=False
        )

        if conforms:
            print(f"  PASS: {file_path}")
        else:
            print(f"  FAIL: {file_path}")
            print(results_text)
            all_valid = False

    return all_valid

if __name__ == "__main__":
    if validate_ontology():
        print("\nAll files passed validation.")
        sys.exit(0)
    else:
        print("\nValidation failed.")
        sys.exit(1)
