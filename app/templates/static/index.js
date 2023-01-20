function getMemes() {
  let memeArr = [];
  fetch(`http://localhost:8000/memes`, {
    method: "GET",
  })
    .then(function (response) {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then(function (data) {
      for (i in data) {
        memeArr.push(data[i]);
      }
      return memeArr;
    });
  return memeArr;
}

function logout() {
  localStorage.clear();
}

window.addEventListener("load", function () {
  let memes = getMemes();
  let token = localStorage.getItem("token");
  let current = 0;
  const img = document.getElementById("image");
  const backBtn = document.getElementById("back");
  const nextBtn = document.getElementById("next");
  const linksDiv = document.getElementById("links");
  const saveBtn = document.getElementById("save");
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
        <a class="nav-link" id="myMemesLink" href="mymemes">My Memes</a>
        </li>
        <li class="nav-item">
        <a class="nav-link" id="logout" href="" onclick="logout()">Logout</a>
        </li>`;
  } else {
    linksDiv.innerHTML = `<a class="nav-link" id="loginLink" href="login">Login</a>`;
  }

  setTimeout(function () {
    img.src = memes[current].url;
    indexCheck(current, memes.length);
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

  saveBtn.addEventListener("click", function () {
    let memeId = memes[current].id;
    console.log(memeId);
    const headers = {
      "Content-Type": "application/json",
      "Access-Control-Origin": "*",
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    };
    fetch(`http://localhost:8000/save/${memeId}`, {
      method: "POST",
      headers: headers,
    }).then(function (response) {
      if (response.ok) {
        window.alert("Meme Saved!");
      }
    });
  });
});
