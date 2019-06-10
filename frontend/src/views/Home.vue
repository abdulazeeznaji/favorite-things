<template>
  <div class="home-page">
    <div class="banner">
      <div class="container">
        <h1 class="logo-font"> Favorite </h1>
        <p>Track your favorites .</p>
      </div>
    </div>
    <div class="container page">
      <div class="row">
        <div class="col-md-9">
          <div class="feed-toggle">
              <router-link
                  :to="{ name: 'home' }"
                  exact
                  class="nav-link"
                  active-class="active"
                >
                  Your favorite list
                </router-link>
          </div>
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "home",
};
</script>
