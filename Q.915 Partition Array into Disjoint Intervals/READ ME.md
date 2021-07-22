<h2>Q.915 Partition Array into Disjoint Intervals</h2><h3>Difficulty rating: Medium</h3><hr><div><p> Given an array nums, <strong> partition </strong> it into two (contiguous) subarrays so that: </p>

<p>
<code> 1.</code> Every element in left is less than or equal to every element in right.

<code> 2.</code> Left and right are non-empty.

<code> 3.</code> Left has the smallest possible size.

<p>Return the length of left after such a partitioning. It is guaranteed that such a partitioning exists.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong>nums = [5, 0, 3, 8, 6]
<strong>Output:</strong> 3
<strong>Explanation:
</strong>left = [5, 0, 3], right = [8, 6]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong>nums = [1, 1, 1, 0, 6, 12]
<strong>Output:</strong> 4
<strong>Explanation:
</strong>left = [1, 1, 1, 0], right = [6, 1, 2]
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3x10<sup>4</sup></code></li>
	<li><code>2 &lt;= nums[i] &lt;= 106</code></li>
	<li><code>1 &lt;= dist &lt;= 10<sup>9</sup></code></li>
	<li> It is <strong> guaranteed </strong>there is at <strong> least one </strong> way to partition nums as described. </li>
</ul>
</div>
