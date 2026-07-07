import { courses } from "./data.js";

/* ---------------------------------------------
   Fetch API using Promise (.then())
--------------------------------------------- */

function fetchUser(id) {
    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(response => response.json())
        .then(user => {
            console.log("Promise User:", user.name);
            return user;
        });
}

fetchUser(1);

/* ---------------------------------------------
   Async / Await
--------------------------------------------- */

async function fetchUserAsync(id) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        const user = await response.json();
        console.log("Async User:", user.name);
    } catch (error) {
        console.log(error);
    }
}

fetchUserAsync(2);

/* ---------------------------------------------
   Simulated API Delay
--------------------------------------------- */

function fetchAllCourses() {

    return new Promise(resolve => {

        setTimeout(() => {

            resolve(courses);

        },1000);

    });

}

/* ---------------------------------------------
   DOM Elements
--------------------------------------------- */

const courseGrid=document.querySelector(".course-grid");

const loading=document.querySelector("#loading");

const totalCredits=document.querySelector("#total-credits");

const notificationList=document.querySelector("#notification-list");

const spinner=document.querySelector("#spinner");

const errorMessage=document.querySelector("#error-message");

const retryButton=document.querySelector("#retry-btn");

/* ---------------------------------------------
   Render Courses
--------------------------------------------- */

function renderCourses(courseArray){

courseGrid.innerHTML="";

courseArray.forEach(course=>{

const article=document.createElement("article");

article.className="course-card";

article.innerHTML=`

<h3>${course.name}</h3>

<p><strong>Code:</strong> ${course.code}</p>

<p><strong>Credits:</strong> ${course.credits}</p>

<p><strong>Grade:</strong> ${course.grade}</p>

`;

courseGrid.appendChild(article);

});

const credits=courseArray.reduce(

(sum,course)=>sum+course.credits,

0

);

totalCredits.textContent=`Total Credits : ${credits}`;

}

/* ---------------------------------------------
   Load Courses after 1 second
--------------------------------------------- */

loading.style.display="block";

fetchAllCourses()

.then(courseData=>{

loading.style.display="none";

renderCourses(courseData);

});

/* ---------------------------------------------
   Promise.all()
--------------------------------------------- */

Promise.all([

fetchUser(1),

fetchUser(2)

])

.then(users=>{

console.log(

"Both Users:",

users[0].name,

users[1].name

);

});

/* ---------------------------------------------
   Reusable Fetch Function
--------------------------------------------- */

async function apiFetch(url){

const response=await fetch(url);

if(!response.ok){

throw new Error("Unable to fetch data.");

}

return await response.json();

}

/* ---------------------------------------------
   Fetch Notifications
--------------------------------------------- */

async function loadNotifications(){

spinner.style.display="block";

notificationList.innerHTML="";

errorMessage.textContent="";

retryButton.style.display="none";

try{

const posts=await apiFetch(

"https://jsonplaceholder.typicode.com/posts?_limit=5"

);

spinner.style.display="none";

posts.forEach(post=>{

const card=document.createElement("div");

card.className="notification-card";

card.innerHTML=`

<h3>${post.title}</h3>

<p>${post.body}</p>

`;

notificationList.appendChild(card);

});

}

catch(error){

spinner.style.display="none";

errorMessage.textContent=

"Something went wrong while loading notifications.";

retryButton.style.display="inline-block";

}

}

loadNotifications();

/* ---------------------------------------------
   Retry Button
--------------------------------------------- */

retryButton.addEventListener("click",()=>{

loadNotifications();

});

/* ---------------------------------------------
   Simulate 404 Error
--------------------------------------------- */

apiFetch(

"https://jsonplaceholder.typicode.com/nonexistent"

)

.catch(()=>{

errorMessage.textContent=

"404 Error handled successfully.";

retryButton.style.display="inline-block";

});

/* ---------------------------------------------
   Axios Interceptor
--------------------------------------------- */

axios.interceptors.request.use(config=>{

console.log(

"API call started:",

config.url

);

return config;

});

/* ---------------------------------------------
   Axios Request
--------------------------------------------- */

async function loadAxiosPosts(){

try{

const response=await axios.get(

"https://jsonplaceholder.typicode.com/posts",

{

params:{

userId:1

},

timeout:5000

}

);

console.log(

"Axios Posts",

response.data

);

}

catch(error){

console.log(error);

}

}

loadAxiosPosts();

/* ---------------------------------------------
Fetch vs Axios

1. Fetch requires response.ok checking.
   Axios throws automatically.

2. Fetch needs response.json().
   Axios parses JSON automatically.

3. Fetch is built into browsers.
   Axios is an external library.
--------------------------------------------- */