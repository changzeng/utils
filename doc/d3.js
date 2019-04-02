// select选择如下元素
d3.select('[hello]')
// <div hell></div>

// d3.entries(object)
// 返回一个包含对象(object)(一个关联数组)中名称以及值(键和值， key and value)的数组 (array)。每一个实体都是有键值对的对象，例如{key: "foo", value: 42}。返回数组的顺序未定义。
// d3.entries({foo: 42， bar: true}); // returns [{key: "foo", value: 42}]
select 
	uid, 
	tid, 
	lesson_id, 
	course_id, 
	relation_type, 
	exam_id, 
	is_correct, 
	title, 
	is_participate, 
	exam_tid_num, 
	difficulty, 
	category, 
	point_list, 
	start_time, 
	submit_time,
	stu_answer
from zyb_basic_stuexam 
where dt='20190317'
	and category=3
	and tid in (383263243, 403994948, 396146038, 396146038, 402375382, 406408737, 406710250, 407914735, 378798056, 382585676, 405503020, 378513619)