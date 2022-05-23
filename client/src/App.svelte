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
  //#region

  let logged = false;
  let login = false;
  let admin = false;
  let news = [[]];

  function loggedAs() {
    fetch("./loggedAs")
      .then((d) => d.text())
      .then((d) => {
        console.log(d);

        if (d == "admin") {
          logged = true;
          admin = true;
        } else if (d == "user") {
          logged = true;
          admin = false;
        } else {
          logged = false;
          admin = false;
        }
        console.log(admin, logged);
      });
  }
  console.log(login);

  loggedAs();

  function logout() {
    console.log("TEST");
    login = false;
    admin = false;
    fetch("./logout")
      .then((d) => d.text())
      .then((d) => {
        console.log(d);

        if (d == "admin") {
          logged = true;
          admin = true;
        } else if (d == "user") {
          logged = true;
          admin = false;
        } else {
          logged = false;
          admin = false;
        }
        console.log(admin, logged);
      });
  }

  ////#region DANE Z BAZY DANYCH

  let sliderChangeTime = 4;
  // let sliderChangeTimeFromChild = 4;

  let headerElems = [{ name: "Elem", url: "xddd" }];

  let article =
    "The cat (Felis catus) is a domestic species of small carnivorous mammal.It is the only domesticated species in the family Felidae and is oftenreferred to as the domestic cat to distinguish it from the wild members of the family. A cat can either be a house cat, a farm cat or a feral cat;the latter ranges freely and avoids human contact. Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries. The cat is similar in anatomy to the other felid species: it has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey. Its night vision and sense of smell are well developed. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling and grunting as well as cat-specific body language. A predator that is most active at dawn and dusk (crepuscular), the cat is a solitary hunter but a social species. It can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small mammals. Cats also secrete and perceive pheromones.";

  //#endregion
  console.log(admin);
  setContext("admin", admin);
  setContext("article", article);
  setContext("headerElems", headerElems);

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
    console.log(root.style.fontFamily);
    console.log(font);
    document.querySelector("body").style.fontFamily = font;
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
    <HeaderAdmin logout={() => logout()} />
    <!-- <HeaderAdmin /> -->
  {:else}
    <HeaderLog logout={() => logout()} />
    <!-- <HeaderLog /> -->
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
