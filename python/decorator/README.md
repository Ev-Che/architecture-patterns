<h1>Functions</h1>
<br>
<p>In Python, functions are the first-class objects, which means that:
<ul>
    <li>Functions are objects — they can be referenced to, passed to a variable<br> 
        and returned from other functions as well.</li>
    <li>Functions can be defined inside another function — an inner function —<br> 
        and can also be passed as an argument to another function.</li>
</ul>
<br>

<h1>Introspection</h1>
In Python Introspection is the ability of an object to know about its own attributes<br>
at runtime. For instance, a function knows its own name and documentation. Let's print<br>
the decorated function name.<br>

<b>print(doubled.__name__)</b> <em>Output: wrapper</em><br>

<p>After being decorated our function has become confused about its identity<br>
because it's being called from wrapper function. To fix this, decorators should<br> 
use the <ins><i>@functools.wraps</i></ins> decorator in wrapper function, which will<br> 
preserve information about the original function. After adding this decorator it will<br> 
return its original name</p>
