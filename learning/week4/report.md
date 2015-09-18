{% data src="../../hackathons/fcq/fcq.clean.json" %}
{% enddata %}

# Report

As a team, answer all the questions the team's members submitted on our
[course forum](https://github.com/bigdatahci2015/forum/issues/14). Each
team member is responsible for one question. But everyone should work together
to come up with a good solution. Your answer should consist of Lodash code
and a brief writeup. Utilize `_.map`, `_.filter`, `_.group` ...etc. Do not
use any for loop.

It is important for everyone to understand all the solutions and make sure you
will be able to independently reproduce these solutions when asked to do so.
Coming up, we will incorporate variations of these questions into a future hackathon
 and you are expected to be capable of reproducing and adapting your solutions.

# Which department has the highest enrollment? by Tristan Wagar

{% lodash %}
var groups = _.groupBy(data, function(college){
    return college['Subject']
})

var courseEnroll = _.mapValues(groups, function(a){
    return _.map(a, function(b){
        return b['N']['ENROLL']
    })
})

var enroll = _.mapValues(courseEnroll, function(enrolls){
    return _.sum(enrolls)
})
return _.pick(enroll, function(number){
    return number == _.max(enroll)
})
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# Which instructor's course has the highest enrollment? by Zhili Yang

{% lodash %}
var groups = _.groupBy(data,function(n){
        return n.Instructors[0].name
})
var enrolls = _.pluck(data,"N.ENROLL")
var biggest = _.max(enrolls)
var bigClass = _.pick(data,_.matchesProperty('N.ENROLL',biggest))

var prof =  _.pluck(bigClass, "Instructors")
var prof = _.pluck(prof[0],'name')
return prof
{% endlodash %}
The instructor with the highest enrollment is {{result}}

# How many courses in IPHY that has 4 credits hours ? by Fadhil Fath

{% lodash %}
var course = _.filter(data, function(n){
	return n['CrsPBADept'] == 'IPHY'
})

var hour = _.filter(course, function(n){
	return n['Hours'] == 4
})

return _.size(hour)
{% endlodash %}

There are {{result}} courses that have 4 credit hours

# Which departments offer the most 4000 level classes? by Brian McKean

{% lodash %}
var groups = _.groupBy(data, function(college){
    return college['Subject']
})

var courseLevels = _.mapValues(groups, function(a){
    return _.map(a, function(b){
        return b['Course']
    })
})
var count = 0
var levelCount = _.mapValues(courseLevels, function(level){
    count = 0
    return _.map(level, function(n){
    	if(n >= 4000 && n < 5000){
    		count++
		}
		return count
    })
})

var result = _.mapValues(levelCount, function(n){
	return _.max(n)
})
return _.pick(result, function(number){
    return number == _.max(result)
})
{% endlodash %}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>
# What instructor has the highest rating? by Andrew Krodinger

{% lodash %}
var groups = _.groupBy(data,function(n){
        return n.Instructors[0].name
})
var ratings = _.pluck(data,"AvgInstructor")
var best = _.max(ratings)
var bestProf = _.pick(data,_.matchesProperty('AvgInstructor',best))

var prof =  _.pluck(bestProf, "Instructors")
prof = _.flatten(prof)
var prof = _.pluck(prof,'name')
return prof
{% endlodash %}

The instructors with the highest ratings are

<table>
{% for x  in result %}
    <tr>
        <td>{{x}}</td>

    </tr>
{% endfor %}
</table>
