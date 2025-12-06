console.log("Hello world");
    function create(title, name, view, monthd, duration, thumbnail){
     document.querySelector(".duration").innerHTML=duration;
    document.querySelector(".title").innerHTML=title;
    if(view>=1000000) view=view/100000 +"M"
    else if(view>=1000) view=view/100000 +"K"
    document.querySelector(".details").innerHTML = name + " . " + view + " views . " + monthd + " months ago";
    document.querySelector(".image").src = thumbnail;
}
create("Introduction to Backend | Sigma Web Dev veido #2", "CodeWithHarry", 560000, 7, "31:22","https://i.ytimg.com/vi/KtL-SQ20Q0s/hqdefault.jpg?sqp=-oaymwEmCKgBEF5IWvKriqkDGQgBFQAAiEIYAdgBAeIBCggYEAIYBjgBQAE=&rs=AOn4CLDPqs5LtUVsb50otOywVTZEmI75fg"); 
 