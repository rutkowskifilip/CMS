<script>
  export let logout = () => {};
  let headerElems = [[]];
  function elementsBase() {
    fetch("./getelements")
      .then((d) => d.json())
      .then((d) => {
        console.log(d);
        headerElems = d;
      });
  }
  elementsBase();
  let string = "";
  const search = () => {
    window.find(string);
  };
</script>

<header>
  <div class="header">
    <nav>
      <a href="#/">Home</a>
      <a href="#/gallery">Gallery</a>
      {#each headerElems as elem}
        <a href="#/">{elem[0]}</a>
      {/each}
      <a on:click={logout}>Logout</a>
      <a href="#/adminPanel">Admin Panel</a>
    </nav>
  </div>
</header>
<input
  type="text"
  id="search"
  bind:value={string}
  on:input={search}
  placeholder="Search.."
/>

<style>
  input#search {
    position: absolute;
    top: 15px;
    right: 10px;
  }
  header {
    color: var(--font-color);
  }
  div.header {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    padding: 20px;
    align-items: center;
  }
  nav {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    font-size: 1rem /* 16px */;
    line-height: 1.5rem /* 24px */;
    justify-content: center;
  }
  a {
    margin-right: 20px /* 20px */;
  }
  a:hover {
    color: var(--font-color2);
  }
  @media (min-width: 768px) {
    div.header {
      flex-direction: row;
      max-width: 768px;
    }
    nav {
      margin-left: auto;
      margin-right: auto;
    }
  }
  @media (min-width: 640px) {
    div.header {
      max-width: 640px;
    }
  }
  @media (min-width: 1024px) {
    div.header {
      max-width: 1024px;
    }
  }

  @media (min-width: 1280px) {
    div.header {
      max-width: 1280px;
    }
  }

  @media (min-width: 1536px) {
    div.header {
      max-width: 1536px;
    }
  }
</style>
