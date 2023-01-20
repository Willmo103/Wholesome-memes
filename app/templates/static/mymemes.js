function getUserMemes() {
  let memeArr = [];
  const headers = {
    "Content-Type": "application/json",
    "Access-Control-Origin": "*",
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  };
  fetch(`http://localhost:8000/save/`, {
    method: "GET",
    headers: headers,
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      for (i in data.memes) {
        console.log(data.memes[i]);
        memeArr.push(data.memes[i]);
      }
      return memeArr;
    });
  console.log(memeArr);
  return memeArr;
}

function logout() {
  localStorage.clear();
  window.location.href("index.html");
}

window.addEventListener("load", function () {
  let token = localStorage.getItem("token");
  if (!token) {
    window.location = "home";
  }
  let current = 0;
  let memes = getUserMemes();
  const img = document.getElementById("image");
  const backBtn = document.getElementById("back");
  const nextBtn = document.getElementById("next");
  const linksDiv = document.getElementById("links");
  const deleteBtn = document.getElementById("save");
  const indexCheck = (index, length) => {
    length -= 1;
    if (index == length) {
      nextBtn.style.visibility = "hidden";
      return;
    }
    if (index == 0) {
      backBtn.style.visibility = "hidden";
      return;
    }
    nextBtn.style.visibility = "visible";
    backBtn.style.visibility = "visible";
  };

  if (token) {
    linksDiv.innerHTML = `
        <li class="nav-item">
        <a class="nav-link" id="home" href="home">Home</a>
        </li>
        <li class="nav-item">
        <a class="nav-link" id="logout" href="" onclick="logout()">Logout</a>
        </li>`;
  } else {
    linksDiv.innerHTML = `<a class="nav-link" id="loginLink" href="login">Login</a>`;
  }

  setTimeout(function () {
    console.log(memes);
    img.src = memes[current].url;
  }, 1000);

  backBtn.addEventListener("click", function () {
    current -= 1;
    if (current < 0) {
      current = 0;
    } else {
      img.src = memes[current].url;
    }
    indexCheck(current, memes.length);
  });

  nextBtn.addEventListener("click", function () {
    if (current >= memes.length - 1) {
      current = memes.length - 1;
    } else {
      current += 1;
      img.src = memes[current].url;
    }
    indexCheck(current, memes.length);
  });

  deleteBtn.addEventListener("click", function () {
    let memeId = memes[current].id;
    console.log(memeId);
    const headers = {
      "Content-Type": "application/json",
      "Access-Control-Origin": "*",
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    };
    fetch(`http://localhost/save/${memeId}`, {
      method: "DELETE",
      headers: headers,
    }).then(function (response) {
      if (response.ok) {
        window.alert("Meme Deleted!");
        location.reload();
      }
    });
  });
});
