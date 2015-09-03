{% import '../../hackathons/classmates/data.html' as data %}

# Report

There are {{ data.comments.length }} students who gave a self-introduction. As a
class, we brainstormed and came up with a long list of further questions we can
ask based on this data. Our team chose to tackle on the following:

# How many people are in computer science?

{% lodash %}
return _.size(_.filter(data.comments, function(n){
	return _.includes(n.body,"Computer Science") || _.includes(n.body, "CS");
}))

{% endlodash %}

{{result}}

# How many people names start with A?

{% lodash %}

var list = _.filter(_.pluck(data.comments, 'body'), function(text){
	var a = text.split("\r\n")[0]
	var name = _.last(text.split("Name:"))
	return name.charAt(1) == 'A'
})

return _.size(list)
{% endlodash %}

{{result}}

# How many people are not a computer science major?

{% lodash %}
return data.comments.length - _.size(_.filter(data.comments, function(n){
	return _.includes(n.body,"Computer Science") || _.includes(n.body, "CS");
}))
{% endlodash %}

{{result}}

# What is the id number of user zhya215?

{% lodash %}

var x = _.filter(data.comments, function(n){
	return _.includes(n.user,"zhya215");
})

var y = _.pluck(x, 'user.id')

console.log(y)

return y

{% endlodash %}

{{result}}
