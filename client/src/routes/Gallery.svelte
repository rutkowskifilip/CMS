<script>
  import { getContext } from "svelte";
  let admin;
  function loggedAs() {
    fetch("./loggedAs")
      .then((d) => d.text())
      .then((d) => {
        console.log(d);

        if (d == "admin") {
          admin = true;
        } else {
          admin = false;
        }
        console.log(admin);
      });
  }

  loggedAs();

  let photos = [[""]],
    comments = [["x"]];
  // let article = "";
  function photosBase() {
    fetch("./getgallery")
      .then((d) => d.json())
      .then((d) => {
        console.log(d);
        photos = d;
      });
  }
  photosBase();
  function commentsBase() {
    fetch("./getcomments")
      .then((d) => d.json())
      .then((d) => {
        console.log(d);
        comments = d;
      });
  }
  commentsBase();
  let article = "";
  function articleCont() {
    fetch("./getarticle")
      .then((d) => d.text())
      .then((d) => {
        console.log(d);
        article = d;
      });
  }
  articleCont();
  //const comments = getContext("comments");

  let editable = false;
  if (admin) {
    editable = true;
  }
  let numberOfPhotos = 4;
  const changeNumberOfPhotos = () => {
    var photos = document.querySelectorAll("div.image");
    photos.forEach((photo) => {
      photo.style.width =
        "calc(" + 100 / numberOfPhotos + "% - " + 64 / numberOfPhotos + "px)";
    });
  };
  function editArticle() {
    console.log("xddd");
    let content = document.getElementById("article").innerText;
    fetch("http://127.0.0.1:5000/editarticle", {
      method: "POST",
      credentials: "include",
      body: JSON.stringify({ content: content }),
      headers: new Headers({ "content-type": "plain/text" }),
      mode: "cors",
    }).then((response) => response.text());
  }
</script>

<section>
  <div class="container">
    <h1 id="title" contenteditable={admin}>Article</h1>
    <p id="article" contenteditable={admin}>{article}</p>
    {#if admin}
      <button on:click={editArticle}>Save</button>
    {/if}
  </div>
</section>
<section>
  <div class="container ">
    <h1>Gallery</h1>
    <div class="photosInRow">
      <p id="photosInRow">Photos in row:</p>

      <select
        name="gallery"
        id="photosInRow"
        bind:value={numberOfPhotos}
        on:change={changeNumberOfPhotos}
      >
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
      </select>
    </div>
    <div class="gallery">
      {#each photos as photo, i}
        <div class="image">
          <img alt="gallery" src={photo[0]} />
          <div class="imgDesc">
            <h2>
              Cat {i + 1}
            </h2>
            <p>photo {i + 1}</p>
          </div>
        </div>
      {/each}
      {#if admin}
        <div style="width:100%">
          <form
            action="http://localhost:5000/addgallery"
            method="post"
            class="addPhoto"
          >
            <label for="url">Photo url:</label>
            <input type="text" name="url" id="url" />

            <input type="submit" value="ADD" />
          </form>
        </div>
      {/if}
    </div>
  </div>
</section>
<section>
  <div class="container">
    <h1>Comments</h1>
    <form
      action="http://localhost:5000/addcomment"
      id="commentForm"
      method="post"
    >
      <textarea name="comment" id="addComment" cols="70" rows="10" />
      <button type="submit" title="Add">Add</button>
    </form>
    {#each comments as comment}
      <div id="comment">
        <div id="author"><h2>{comment[0]}</h2></div>
        <div id="content"><p>{comment[1]}</p></div>
      </div>
    {/each}
  </div>
</section>

<style>
  select#photosInRow {
    width: fit-content;
    height: 32px;
  }
  p#photosInRow {
    width: fit-content;
    margin-right: 10px;
  }
  div.photosInRow {
    width: 90%;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  input#url,
  label {
    width: 80%;
    margin-left: 10%;
  }
  form.addPhoto {
    width: calc(25% - 16px);
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
  }
  div.gallery {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: left;
  }
  #comment {
    width: 90%;
    display: flex;
    flex-direction: column;
    padding: 10px;
    height: fit-content;
    margin-top: 32px;
    padding-left: 32px /* 32px */;
    padding-right: 32px /* 32px */;

    text-align: center;
    position: relative;
  }
  #author {
    width: 100%;
    text-align: left;
    height: fit-content;
    padding: 5px;
  }
  #content {
    border-radius: 8px /* 8px */;
    background-color: var(--divs-color2);
    width: 100%;
    text-align: justify;

    height: fit-content;
    padding: 5px;
  }
  #commentForm {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 50%;
  }

  p {
    line-height: 1.625;
  }
  div.imgDesc {
    padding-left: 32px /* 32px */;
    padding-right: 32px /* 32px */;
    padding-top: 40px /* 40px */;
    padding-bottom: 40px /* 40px */;
    position: relative;
    z-index: 10;
    width: 100%;
    border: 4px solid;
    transition: opacity 0.3s;
    border-color: var(--font-color);
    opacity: 0;

    background-color: var(--divs-color);
  }
  div.imgDesc:hover {
    opacity: 1;
  }
  img {
    position: absolute;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }
  div.image {
    display: flex;
    position: relative;
    height: 320px;
    width: calc(25% - 16px);
  }
  section {
    color: var(--font-color);
  }
  h1 {
    font-size: 1.5rem /* 24px */;
    line-height: 2rem /* 32px */;
    font-weight: 500;
    margin-bottom: 16px;
    --tw-text-opacity: 1;
    color: var(--font-color2);
  }
  div.container {
    width: 100%;
    padding-top: 96px /* 96px */;
    padding-bottom: 96px /* 96px */;
    padding-left: 32px;
    padding-right: 32px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  h2 {
    letter-spacing: 0.1em;
    font-size: 0.875rem /* 14px */;
    line-height: 1.25rem /* 20px */;
    font-weight: 500;

    color: var(--btn-color);
  }
  @media (min-width: 640px) {
    div.container {
      max-width: 640px;
    }
    h1 {
      font-size: 1.875rem /* 30px */;
      line-height: 2.25rem /* 36px */;
    }
  }

  @media (min-width: 768px) {
    div.container {
      max-width: 768px;
    }
  }

  @media (min-width: 1024px) {
    div.container {
      max-width: 1024px;
    }
  }

  @media (min-width: 1280px) {
    div.container {
      max-width: 1280px;
    }
  }

  @media (min-width: 1536px) {
    div.container {
      max-width: 1536px;
    }
  }
  button:focus,
  input[type="submit"]:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
  }
  button:hover,
  input[type="submit"]:hover {
    background-color: var(--btn-hov-color);
  }
  button,
  input[type="submit"] {
    color: white;

    background-color: var(--btn-color);
    border: 0;
    padding-top: 8px /* 8px */;
    padding-bottom: 8px /* 8px */;
    border-radius: 4px /* 4px */;
    font-size: 1.125rem /* 18px */;
    line-height: 1.75rem /* 28px */;
    padding-left: 24px /* 24px */;
    padding-right: 24px /* 24px */;
  }
</style>
