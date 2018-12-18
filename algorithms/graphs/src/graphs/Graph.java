package graphs;

import java.util.Set;

public class Graph
{
    public Set<Vertex> vertices;
    public Set<Edge> edges;
    
    public Graph(Set<Vertex> vertices, Set<Edge> edges)
    {
    	this.vertices = vertices;
    	this.edges = edges;
    }
}