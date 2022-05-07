<script>
  import Router from "svelte-spa-router";
  import Home from "./routes/Home.svelte";
  import Gallery from "./routes/Gallery.svelte";
  import SignIn from "./routes/SignIn.svelte";
  import SignUp from "./routes/SignUp.svelte";
  import Settings from "./components/Settings.svelte";
  import NotFound from "./routes/NotFound.svelte";
  import AdminPanel from "./routes/AdminPanel.svelte";
  import Footer from "./components/Footer.svelte";
  import Header from "./components/Header.svelte";
  import HeaderLog from "./components/HeaderLog.svelte";
  import HeaderAdmin from "./components/HeaderAdmin.svelte";

  ////#region DANE Z BAZY DANYCH
  let logged = false;
  let admin = false;
  let sliderChangeTime = 4;
  let sliderChangeTimeFromChild = 4;

  let slides = [
    {
      img: "https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg",
      content: "XDDDDDDDDDDDD",
    },
    {
      img: "https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg",
      content: "XDDDDDDDDDDDD",
    },
    {
      img: "https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg",
      content: "XDDDDDDDDDDDD",
    },
    {
      img: "https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg",
      content: "XDDDDDDDDDDDD",
    },
    {
      img: "https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg",
      content: "XDDDDDDDDDDDD",
    },
  ];

  let news = [
    { title: "a", content: "aaa" },
    { title: "b", content: "bbb" },
    { title: "c", content: "ccc" },
    { title: "c", content: "ccc" },
  ];

  let headerElems = [
    { name: "Elem", url: "xddd" },
    { name: "Elem", url: "xddd" },
  ];

  //#endregion

  setContext("news", news);
  function changeTime() {
    sliderChangeTime = sliderChangeTimeFromChild;
    console.log(sliderChangeTime);
  }
  let theme = "light";
  let font = "";
  let fontSize = 1;
  let bgColor = "";
  let fontColor = "";
  let fontColor2 = "";
  let divsColor = "";
  let divsColor2 = "";
  import { setContext } from "svelte";

  setContext("admin", admin);

  setContext("headerElems", headerElems);

  setContext("slides", slides);
  let root = document.documentElement;
  function changeColors() {
    console.log(theme);

    if (theme == "dark") {
      root.style.setProperty("--bg-color", "#1d3040");
      root.style.setProperty("--font-color", "#bfc2c7");
      root.style.setProperty("--font-color2", "#ffffff");
      root.style.setProperty("--divs-color", "#0084f6");
      root.style.setProperty("--divs-color2", "rgba(00,220,243,0.75)");
    } else if (theme == "light") {
      root.style.setProperty("--bg-color", "#f2eee2");
      root.style.setProperty("--font-color", " rgb(75, 85, 99)");
      root.style.setProperty("--font-color2", "rgb(17, 24, 39)");
      root.style.setProperty("--divs-color", "white");
      root.style.setProperty("--divs-color2", "rgba(243, 244, 246, 0.75)");
    }
  }
  function changeFont() {
    root.style.fontFamily = font;
  }
  function changeSize() {
    root.style.fontSize = fontSize + "rem";
  }
  function changeTheme() {
    console.log("changing");
    root.style.setProperty("--bg-color", bgColor);
    root.style.setProperty("--font-color", fontColor);
    root.style.setProperty("--font-color2", fontColor2);
    root.style.setProperty("--divs-color", divsColor);
    root.style.setProperty("--divs-color2", "rgba(" + divsColor2 + ",0.75)");
  }
</script>

{#if logged}
  {#if admin}
    <HeaderAdmin />
  {:else}
    <HeaderLog />
  {/if}
{:else}
  <Header />
{/if}
<Settings
  changeColors={() => changeColors()}
  bind:theme
  changeFont={() => changeFont()}
  bind:font
  changeSize={() => changeSize()}
  bind:fontSize
  changeTheme={() => changeTheme()}
  bind:bgColor
  bind:fontColor
  bind:fontColor2
  bind:divsColor
  bind:divsColor2
/>
<Router
  routes={{
    "/": Home,
    "/gallery": Gallery,
    "/signin": SignIn,
    "/signup": SignUp,
    "/adminPanel": AdminPanel,
    "*": NotFound,
  }}
/>
<Footer />

<style>
  :global(:root) {
    --bg-color: #f2eee2;
    --btn-color: rgb(99, 102, 241);
    --btn-hov-color: rgb(79, 70, 229);
    --font-color: rgb(75, 85, 99);
    --font-color2: rgb(17, 24, 39);
    --divs-color: white;
    --divs-color2: rgba(243, 244, 246, 0.75);
  }
  :global(body) {
    background-color: var(--bg-color);
    color: #0084f6;
    transition: background-color 0.3s;
    margin: 0;
    padding: 0;
  }
</style>
