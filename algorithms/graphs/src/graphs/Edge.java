package graphs;

public class Edge 
{
	Vertex vert1;
	Vertex vert2;
	private int d;
	
	public Edge(Vertex v1, Vertex v2, int distance)
	{
		vert1 = v1;
		vert2 = v2;
		d = distance;
	}
	
	public int getDistance()
	{
		return this.d;
	}
}
