import pytest
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, OWL

BEAST = Namespace("http://example.org/beast-mode#")


@pytest.fixture
def ontology_graph():
    g = Graph()
    g.parse("beast_mode_ontology.ttl", format="turtle")
    return g


@pytest.fixture
def examples_graph():
    g = Graph()
    g.parse("beast_mode_examples.ttl", format="turtle")
    return g


def test_ontology_loads(ontology_graph):
    """Test that the ontology loads without error."""
    assert len(ontology_graph) > 0


def test_agent_class_exists(ontology_graph):
    """Test that the Agent class is defined."""
    assert (BEAST.Agent, RDF.type, OWL.Class) in ontology_graph


def test_capability_class_exists(ontology_graph):
    """Test that the Capability class is defined."""
    assert (BEAST.Capability, RDF.type, OWL.Class) in ontology_graph


def test_task_class_exists(ontology_graph):
    """Test that the Task class is defined."""
    assert (BEAST.Task, RDF.type, OWL.Class) in ontology_graph


def test_examples_load(examples_graph):
    """Test that the examples load without error."""
    assert len(examples_graph) > 0


def test_agent_has_capability(examples_graph):
    """Test that the example agent has a capability."""
    agent = BEAST["agent-code-reviewer"]
    # We check if there is any capability assigned
    capabilities = list(examples_graph.objects(agent, BEAST.hasCapability))
    assert len(capabilities) > 0


def test_inference_chain(examples_graph, ontology_graph):
    """
    Test the inference: Agent -(hasCapability)-> Cap -(enablesTask)-> Task
    Implies: Agent can perform Task.

    Note: Standard rdflib does not doOWL inference automatically.
    We manually check the chain here to verify the data structure supports it.
    """
    agent = BEAST["agent-code-reviewer"]

    # manual inference simulation
    capabilities = list(examples_graph.objects(agent, BEAST.hasCapability))
    tasks = []
    for cap in capabilities:
        tasks.extend(examples_graph.objects(cap, BEAST.enablesTask))

    assert len(tasks) > 0
    # Ideally, we'd check if specific tasks are enabled.
    task_ids = [t.split("#")[-1] if "#" in str(t) else str(t) for t in tasks]
    # Based on beast_mode_examples.ttl
    assert any("task-analyze-complexity" in t for t in task_ids)
