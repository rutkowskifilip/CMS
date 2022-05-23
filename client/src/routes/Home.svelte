<script>
  import { getContext } from "svelte";
  import { get } from "svelte/store";
  import { onMount } from "svelte";
  import { hslide } from "../hslide.js";
  let admin,
    time = 4,
    news = [["X", "D"]],
    slides = [[""]];

  function articlesBase() {
    fetch("./articlesbase")
      .then((d) => d.json())
      .then((d) => {
        console.log(d);
        news = d;
      });
  }
  function getTime() {
    fetch("./gettime")
      .then((d) => d.text())
      .then((d) => {
        console.log(d);
        time = d;
        setInterval(() => {
          next();
          console.log(time);
        }, time * 1000);
      });
  }

  getTime();
  articlesBase();
  let photos = [[""]];
  function photosBase() {
    fetch("./photosbase")
      .then((d) => d.json())
      .then((d) => {
        console.log(d);
        slides = d;
      });
  }
  photosBase();

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
  // const slides = getContext("slides");

  let cur = 0;
  const sliderChangeTime = getContext("sliderChangeTime");
  //console.log(sliderChangeTime);
  function changeSlide(slide) {
    cur = slide;
  }

  const clamp = (number, min, max) => Math.min(Math.max(number, min), max);
  const transition_args = {
    duration: 200,
  };

  function prev(e) {
    if (cur == 0) {
      cur = slides.length;
    }
    cur = clamp(--cur, 0, slides.length - 1);
  }

  function next(e) {
    if (cur == slides.length - 1) {
      cur = -1;
    }
    cur = clamp(++cur, 0, slides.length - 1);
  }

  const ARROW_LEFT = 37;
  const ARROW_RIGHT = 39;
  function handleShortcut(e) {
    if (e.keyCode === ARROW_LEFT) {
      prev();
    }
    if (e.keyCode === ARROW_RIGHT) {
      next();
    }
  }
  let editable = admin;

  let testowa_zmienna = "";
</script>

<svelte:window on:keyup={handleShortcut} />

<div class="extra-outer-wrapper">
  <!-- <h1>{testowa_zmienna}</h1> -->
  <div class="outer-wrapper">
    <div class="inner-wrapper">
      {#each slides as slide, id}
        {#if id === cur}
          <div
            class="slide"
            in:hslide={transition_args}
            out:hslide={transition_args}
          >
            <div class="content">
              <h2>Description</h2>
              <p>{slide[1]}</p>
            </div>
            <img src={slide[0]} alt="" />
          </div>
        {/if}
      {/each}
      <div class="controls">
        <button on:click={() => prev()}> &lt; </button>
        <button on:click={() => next()}> &gt; </button>
      </div>
    </div>
  </div>
</div>

<div class="dots">
  {#each slides as slide, i}
    <button
      on:click={() => changeSlide(i)}
      class="dot"
      class:selected={cur == i}>{i + 1}</button
    >
  {/each}
</div>

<div id="news">
  {#each news as onenews, i}
    <div class="oneNews">
      <h2>News {i + 1}</h2>
      <h1 contenteditable={admin}>
        {onenews[0]}
      </h1>
      <p contenteditable={admin}>{onenews[1]}</p>
      <a href="/"
        >Learn More
        <svg
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M5 12h14" />
          <path d="M12 5l7 7-7 7" />
        </svg>
      </a>
      <div class="elem" />
      <br />
      {#if admin}
        <button type="submit">Save</button>
      {/if}
    </div>
  {/each}
  {#if admin}
    <form
      action="http://localhost:5000/addarticle"
      method="post"
      class="addNews"
    >
      <div style="width:100%">
        <label for="title">Title:</label>
        <input type="text" name="title" id="title" />
      </div>
      <div>
        <label for="content">Content:</label>
        <textarea name="content" id="content" cols="40" rows="5" />
      </div>
      <p><input type="submit" value="submit" /></p>
    </form>
  {/if}
</div>

<style>
  svg {
    width: 1rem;
    height: 1rem;
    margin-left: 0.5rem;
  }
  input[type="submit"] {
    height: 40px;
    width: 400px;
  }
  form.addNews {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 32px;
    margin-top: 32px;
    height: 100%;
    width: 384px;
    background-color: var(--divs-color2);

    padding-right: 32px /* 32px */;
    border-radius: 8px /* 8px */;
    text-align: center;
    position: relative;
  }
  textarea,
  input {
    width: 100%;
  }
  img {
    width: 100%;
    height: 100%;
  }
  button,
  input[type="submit"] {
    background: transparent;
    color: #fff;
    border-color: transparent;

    height: 3.2rem;
    background: var(--btn-color);
    margin-top: 5px;
  }

  input[type="submit"]:hover,
  input[type="submit"]:focus,
  button:hover,
  button:focus {
    background: rgba(0, 0, 0, 0.5);
  }

  .dots {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 8px;
  }

  .dot {
    width: 8px;
    height: 8px;
    background: #000;
    border-radius: 100%;
    font-size: 0;
    margin: 0.3rem;
    opacity: 0.3;
  }

  .dot.selected {
    opacity: 1;
  }

  .extra-outer-wrapper {
    width: 80%;
    margin: 0 auto;
    height: 300px;
  }

  .outer-wrapper {
    width: 100%;
    height: 100%;
    padding: 0 0 56.25%;
    position: relative;
  }

  .inner-wrapper {
    height: 300px;
    width: 100%;
    display: flex;
    position: absolute;
  }

  .controls button:first-child {
    position: absolute;
    left: 0;
    top: calc(50% - 1.2rem);
  }

  .controls button:last-child {
    position: absolute;
    right: 0;
    top: calc(50% - 1.2rem);
  }

  .slide {
    flex: 1 0 auto;
    width: 100%;
    height: 100%;
    background: var(--divs-color);
    align-items: center;
    justify-content: center;
    display: flex;
    text-align: center;
    font-weight: bold;
    font-size: 2rem;
    color: white;
  }

  .controls {
    text-align: center;
    width: 100%;
    display: block;
  }
  .content {
    width: 92%;
    height: calc(100% - 8px);
    left: 4%;
    position: absolute;
    opacity: 0;
    z-index: 10;
    border: 4px solid;
    background-color: var(--divs-color);
    border-color: var(--font-color);
    z-index: 10;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    color: var(--font-color);
    transition: opacity 0.3s;
  }
  .content:hover {
    opacity: 0.75;
  }
  div.elem {
    text-align: center;
    margin-top: 8px;
    line-height: 1;
    display: flex;
    justify-content: center;
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding-top: 16px /* 16px */;
    padding-bottom: 16px /* 16px */;
  }
  a,
  label {
    color: var(--btn-color);
    display: inline-flex;
    align-items: center;
  }
  p {
    line-height: 1.625;
    margin-bottom: 12px /* 12px */;
  }
  h2 {
    letter-spacing: 0.1em;
    font-size: 0.75rem /* 12px */;
    line-height: 1rem /* 16px */;
    font-weight: 500;
    color: var(--font-color);
    margin-bottom: 4px /* 4px */;
  }
  @media (min-width: 640px) {
    h1 {
      font-size: 1.5rem /* 24px */;
      line-height: 2rem /* 32px */;
    }
  }
  h1 {
    font-weight: 500;
    font-size: 1.25rem /* 20px */;
    line-height: 1.75rem /* 28px */;

    color: var(--font-color2);
    margin-bottom: 12px /* 12px */;
  }
  div.oneNews {
    margin-top: 32px;
    height: 100%;
    width: 384px;
    background-color: var(--divs-color2);

    padding-left: 32px /* 32px */;
    padding-right: 32px /* 32px */;
    padding-top: 64px /* 64px */;
    padding-bottom: 96px /* 96px */;
    border-radius: 8px /* 8px */;
    text-align: center;
    position: relative;
  }
  div#news {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    flex-wrap: wrap;
  }
</style>
