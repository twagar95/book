# Report

Use only Javascript and SVG to produce a data analysis / visualization report.

# Authors

This report is prepared by
* [Tristan Wagar](https://www.github.com/twagar95)
* [Sushant Mittal](www.github.com/sumi6109)

<a name="top"/>
<div id="autonav"></div>

# What is the spread of intro level courses between departments?

{% data src="../fcq/fcq.clean.json" %}
{% enddata %}

{% viz %}

{% title %}

Which department has the least amount of intro level courses?

{% solution %}

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
    	if(n >= 1000 && n < 2000){
    		count++
		}
		return count
    })
})

var result = _.mapValues(levelCount, function(n){
	return _.max(n)
})

var result1 = _.map(result,function(name,count){
  return { courseCount:name ,departmentName:count}
})


function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 20
}

function computeWidth(d, i) {
    return d.courseCount * (400/128)
}

function computeY(d, i) {
    return 20 * i
}

function computeColor(d, i) {
    return 'red'
}

function computeLabel(d, i){
	return d.departmentName
}

var viz = _.map(result1, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
                color: computeColor(d, i),
                label: computeLabel(d, i)
            }
         })
console.log(viz)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}

<g transform="translate(0 ${d.y})">
    <rect         
         x="${d.x}"
         width="${d.width}"
         height="20"
         style="fill:${d.color};
                stroke-width:3;
                stroke:rgb(0,0,0)" />
<text transform= "translate(0 15)">${d.label}</text>
</g>

{% endviz %}

Use the warmup exercise as the template to produce an answer here.

# Sushant

# What is distribution of Number of Hrs worked for each department ?

{% viz %}

{% title %}
What is distribution of Number of Hrs worked for each department?

{% solution %}

var grps= _.groupBy(data,'CrsPBADept')

var values =_.mapValues(grps,function(d){
hrs= _.pluck(d,'Workload')
var hrs_string=_.map(hrs,function(d){return d.Hrs_Wk})
var total_hrs=_.map(hrs_string,function(d){ return d.split('-')[1]})
return _.sum(total_hrs)
})
var values =_.pick(values,function(d){return d>0})
console.log(values)
var data1=_.map(values,function(group,name){return { course_name:name ,hrswork:group}})
var max= _.max(_.pluck(data1,'hrswork'))
//console.log(data1)


function computeX(d, i) {
return 0
}

function computeHeight(d, i) {
return 20
}

function computeY(d, i) {
return 20*i
}
function computeWidth(d, i) {
return d.hrswork/4
}
function computeColor(d, i) {
return 'red'
}
function computeName(d, i) {
return d.course_name
}

var viz = _.map(data1, function(d, i){
return {
x: computeX(d, i),
y: computeY(d, i),
height: computeHeight(d, i),
color: computeColor(d, i),
width: computeWidth(d,i),
name:computeName(d,i)
}
})
console.log(data1)

var result = _.map(viz, function(d){
// invoke the compiled template function on each viz data
return template({d: d})
})
return result.join('\n')



{% template %}

<g transform="translate(0 ${d.y})">
<rect
width="${d.width}"
height="20"
style="fill:${d.color};
stroke-width:3;
stroke:rgb(0,0,0)" />
<text transform="translate(0 15)">
${d.name}
</text>
<text transform="translate(80 15)">
${d.width*4}
</text>
</g>
{% endviz %}

