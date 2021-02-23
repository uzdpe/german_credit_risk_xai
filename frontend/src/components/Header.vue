<template>
  <div>
     <!--<img alt="logo" src="../assets/consileon_logo.png" class="logo" -->
    <div class="text">
      <h2> XAI Dashboard </h2><br>
      
      <div id="nav">
        <router-link to="/Intro">1. Intro</router-link>
        <router-link to="/testphase">2. Testphase</router-link>
        <router-link to="/training">3. Training</router-link>
        <router-link to="/prediction">4. Prediction</router-link>
        <router-link to="/global">4.1 Global Explanation</router-link>
        <router-link to="/instance">4.2 Local Explanation</router-link>
        <router-link to="/survey">5. Survey</router-link>


      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped>
  .text {
    float: top;
    background: rgba(255, 255, 255, 0.76);
    color: #000032;
    text-align: center;
    font-size: 30px;
    padding: 50px;
  }
  .text a {
    color: #000032;
    padding-right: 5px;

    text-decoration: none;
    margin-top: 200px;
    margin-right: 100px;
    font-size: 20px;
  }
  .logo{
    float: left;
    margin-left: 100px;
    margin-right: 100px;
    margin-top: 100px;
    width: 10%;
  }
</style>
