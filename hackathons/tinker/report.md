# Q: What are the number of commits?

## Data

{% set data = [["fouber/blog",15],["michaeldfallen/Git-radar",12],["flarum/flarum",42],["girlieMac/RPi-KittyCam",52],["Chneukirchen/Nq",24]]%}

<table>
    <tr> 
    	<td> Repository </td>
    	<td> Commits </td>
    </tr>
    {% for rows in data %}
        <tr>
            <!-- Add your code here  -->
            {% for columns in rows  %}
                <td>{{columns}}</td>
            {% endfor %}
        </tr>
    {% endfor %}
</table>

## Visualization

{% set numbers = [15,12,42,52,24] %}

<svg width="423" height="200">
{% for number in numbers %}
    <rect y="{{loop.index * 20}}" width="{{number}}" height="15" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>

## Recommendation

We recommended SVG because it is a lightweight way to bring visualization of data to our git book. It is easily
implemented into the markdown files and has concise and clear syntax, essentially HTML.
