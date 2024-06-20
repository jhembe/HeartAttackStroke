<template>
    <header class="header">
      <div class="container">
        <div class="logo">
          <!-- <img src="@/assets/logo.png" alt="Logo" /> -->
          <ul><li><a href="#">Cardiac Screening</a></li></ul>
        </div>
        <nav class="nav">
          <ul>
            <li><a href="#about">Heart Attack</a></li>
            <li><a href="#projects">Stroke</a></li>
          </ul>
        </nav>
      </div>
    </header>
  </template>
  
  <script>
  import { onMounted } from 'vue';
  import { gsap } from 'gsap';
  
  export default {
    name: 'AppHeader',
    setup() {
      onMounted(() => {
        const tl = gsap.timeline({ defaults: { duration: 1, ease: 'power3.out' } });
        tl.from('.header', { opacity: 0, y: -50 })
          .from('.logo img', { opacity: 0, y: -20 }, '-=0.5')
          .from('.nav li', { opacity: 0, y: -20, stagger: 0.2 }, '-=0.5');
      });
    },
  };
  </script>

  
  <style scoped>


  .header {
    background-color: #333;
    color: white;
    height: 50px;
    padding: 5px 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .container {
    /* background-color: red; */
    display: flex;
    height: 90%;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;

  }
/*   
  .logo img {
    height: 50px;
  } */
  
  .nav ul {
    list-style: none;
    display: flex;
    margin: 0;
    padding: 0;
  }
  
  .nav li {
    margin-left: 20px;
  }
  
  div.logo{
    /* background-color: greenyellow; */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  div.logo ul li{
    margin-top: 16px;
    /* background-color: red; */
  }

  div.logo ul{
    /* background-color: blue; */
    display: flex;
    text-align: center;
    justify-content: center;
    align-items: center;

  }

  .logo a{
    text-decoration: none;
    color:white;
    font-size: 20px;
    font-weight: bold;
  }
  .nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease;
  }
  
  .nav a:hover {
    color: #42b983;
  }
  </style>
  