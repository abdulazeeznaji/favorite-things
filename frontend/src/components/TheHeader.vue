<template>
  <nav class="navbar navbar-light">
    <div class="container">
      <router-link class="navbar-brand" :to="{ name: 'home' }">
        Favorite
      </router-link>
      <ul class="nav navbar-nav pull-xs-right">
        <li class="nav-item">
          <router-link
                  class="nav-link"
                  active-class="active"
                  exact
                  :to="{ name: 'home' }"
          >
            Home
          </router-link>
        </li>
        <li class="nav-item">
          <router-link
                  class="nav-link"
                  active-class="active"
                  exact
                  :to="{ name: 'login' }"
          >
            <i class="ion-compose"></i>Sign in
          </router-link>
        </li>
        <li class="nav-item">
          <router-link
                  class="nav-link"
                  active-class="active"
                  exact
                  :to="{ name: 'register' }"
          >
            <i class="ion-compose"></i>Sign up
          </router-link>
        </li>
        <li class="nav-item">
          <router-link
                  class="nav-link"
                  active-class="active"
                  exact
                  :to="{ name: 'home' }"
          >
            Home
          </router-link>
        </li>
        <li class="nav-item">
          <router-link
                  class="nav-link"
                  active-class="active"
                  :to="{ name: 'favorite-edit' }"
          >
            <i class="ion-compose"></i>&nbsp;New Favorite
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'
  export default {
    name: 'RwvHeader',
    computed: {
      ...mapGetters(['currentUser'])
    }
  }
</script>
