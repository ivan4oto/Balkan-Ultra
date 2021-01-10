<template>
<div>
  
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-container>
      <b-navbar-brand to="/">Начало</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/Register">Регистрация</b-nav-item>
        <b-nav-item to="Athletes">Участници</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="Резултати" right>
          <b-dropdown-item to="Results">2020</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item to="About">Информация</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
    </b-container>
  </b-navbar>
  
</div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
 .navbar.navbar-dark.bg-dark{
    background-color: #3a3547!important;
    font-family: 'SPArielBG';
 }
::v-deep .nav-link {
   color: rgb(216, 240, 172)!important;
}
.navbar-brand {
   color: rgb(235, 231, 12)!important;
}
.nav-link:hover, .navbar-brand:hover {
   background-color: #5e4b63!important;
}
</style>