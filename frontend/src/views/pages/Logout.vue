<template>
  <div class="bg-light min-vh-100 d-flex flex-row align-items-center">
    <CContainer>
      <CRow class="justify-content-center">
        <CCol :md="8">
          <CCardGroup>
            <CCard class="p-4">
              <CCardBody>
                <h1>Ciao... we will miss YOU!!!</h1>
                <CNavLink
                  href="#/pages/login"
                  v-if="!this.$store.state.isAuthenticated"
                  >Login</CNavLink
                >
                <!-- <div id="nav">
                <CLink to="#/pages/login">Login</CLink>
                </div> -->

                <!-- <a class="" to="/log-in" v-if="!this.$store.state.isAuthenticated">LogIn</a> -->
              </CCardBody>
            </CCard>
          </CCardGroup>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
export default {
  name: 'LogOut',
  data() {
    return {}
  },
  mounted() {
    this.$store.commit('removeToken')
    console.log('Logout')
  },
  methods: {},
  computed: {},
}
</script>

<style lang="css" scoped></style>
