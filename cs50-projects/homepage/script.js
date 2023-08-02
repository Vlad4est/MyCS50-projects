let page = document.body.id;
switch (page)
{
    
    case "quiz":
    document.querySelector("#quiz-form").addEventListener("submit", function (event) {
    event.preventDefault();
    let q1 = document.getElementById("question1").value.toLowerCase();
    let q2 = document.getElementById("question2").value.toLowerCase();
    let q3 = document.getElementById("question3").value.toLowerCase();
    let q4 = document.getElementById("question4").value.toLowerCase();
    let q5 = document.getElementById("question5").value.toLowerCase();
    let score = 0;
    if (q1 == "vlad") {
        score++;
    }
    if (q2 == "bucharest, romania") {
        score++;
    }
    if (q3 == "it" || q3 == "nationalism" || q3 == "gaming" || q3 == "football" || q3 == "programming") {
        score++;
    }
    if (q4 == "steaua" || q4 == "steaua bucharest")
    {
        score++;
    }
    if (q5 == "csgo" || q5 == "valorant" || q5 == "league of legends")
    {
        score++;
    }
    alert(`Score: ${score}/5`);
    });



    case "contact":
    document.querySelector("#form").addEventListener("submit", function(event) {
    event.preventDefault();
    let name = document.getElementById("nameInput").value;
    let email = document.getElementById("emailInput").value;
    let message = document.getElementById("messageInput").value;
    console.log("Hello");
    alert(`Message was submitted!\nName: ${name}\nEmail: ${email}`);
});
}



