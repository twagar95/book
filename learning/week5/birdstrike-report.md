{% data src="birdstrike.json" %}
{% enddata %}

# Report

As a team, answer a subset of the questions submitted during the hackathon.
But instead of using Tableau, you will need to write Javascript/Lodash code
to derive your answers. Similar to before, each team member is responsible for
one question. But everyone should work together to come up with a good solution.
Your answer should consist of Lodash code and a brief writeup.
Utilize `_.map`, `_.filter`, `_.group` ...etc. Do not se any for loop.

This time, the data is not already prepared for you in a nice JSON format. You
will need to do it on your own, replacing the placeholder `birdstrike.json` with
real data.

# Which airport has the highest number struck? by twagar95

{% lodash %}
var groups = _.groupBy(data, function(n){
    return n['Airport: Name']
})

var valuedGroups = _.values(groups)
var result = _.chain(valuedGroups)
                .map(function(arr){
                    return [arr[0]["Airport: Name"], arr.length]
                })
                .reduce(function(n, p){
                    if ((n[1] > p[1]) && (n[0] != "UNKNOWN")) { return n; } else {return p; }
                }).value()

return result
{% endlodash %}
{{result}}

# What states cost the airlines the most money? by SatchelSpencer

{% lodash %}
//What states cost the airlines the most money?
return _.chain(data).groupBy('Origin State').mapValues(function(state){
    return _.reduce(state, function(sum, incident){
        return sum+parseInt(incident['Cost: Total $'].toString().replace(',', ''));
    }, 0);
}).pairs().sortByOrder('1', 1).object().value();
{% endlodash %}

<table>

  <tr>
      <td>Height</td>
      <td>Number of birds hit</td>
  </tr>
{% for key, value in result %}
  <tr>
      <td>{{key}}</td>
      <td>{{value}}</td>
  </tr>
{% endfor %}
</table>

# What is the frequency of bird strikes at various height ranges ? by sumi6109

{% lodash %}

var data_poistive=_.filter(data,function(r){return parseInt(r['Feet above ground'])> 0})

var grps =_.groupBy(data_poistive,function(d){return d['Feet above ground']})
var result=_.mapValues(grps,function(t){return t.length})

var sorted = _.sortBy(_.pairs(result), function(d) {
 
    return parseInt(d[0].replace(',', ''));
});
var desc = _(sorted).value()
return desc
//return result
{% endlodash %}
<table>

  <tr>
      <td>Height</td>
      <td>Number of birds hit</td>
  </tr>
{% for key, value in result %}
  <tr>
      <td>{{key}}</td>
      <td>{{value}}</td>
  </tr>
{% endfor %}
</table>

# What are the top 5 bird species that are involved? by nicolele

// What are the top 5 bird species that are involved?

{% lodash %}
var clean = _.reject(data, function(n){
    return _.includes(n['Wildlife: Species'], 'Unknown')
})

var groups = _.groupBy(clean, function(d){
    return d['Wildlife: Species']   
})

var birds = _.pairs(_.mapValues(groups, function(value){
    return value.length
}))

var top = _.sortBy(birds, function(n) {
    return n[1]
}).reverse()

return _.slice(top, [start=0], [end=5])
{% endlodash %}

{{ result | json }}

# What Airline loses the most money to bird strikes every year? by John

{% lodash %}
var groups = _.groupBy(data, function(n){
    return n['Aircraft: Airline/Operator']
})
var pairs =  _.pairs(_.mapValues(groups, function(item){
  var costs =   _.map(item, function(value){    
    return parseInt(value['Cost: Total $'].toString().replace(',', ''))   })
  return _.sum(costs)
  
  }))
var top = _.sortBy(pairs, function(n){
  return n[1] 
  }).reverse()
top = _.slice(top, [start =0], [end=10])

return top
{% endlodash %}

<table>

  <tr>
      <td>Height</td>
      <td>Total Cost</td>
  </tr>
{% for key, value in result %}
  <tr>
      <td>{{key}}</td>
      <td>{{value}}</td>
  </tr>
{% endfor %}
</table>
