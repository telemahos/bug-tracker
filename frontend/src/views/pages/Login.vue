<template>
  <div class="bg-light min-vh-100 d-flex flex-row align-items-center">
    <CContainer>
      <CRow class="justify-content-center">
        <CCol :md="8">
          <CCardGroup>
            <CCard class="p-4">
              <CCardBody>
                <CForm class="row g-3" @submit="submitForm">
                  <h1>Login</h1>
                  <p class="text-medium-emphasis">Sign In to your account</p>
                  <CInputGroup class="mb-3">
                    <CInputGroupText>
                      <CIcon icon="cil-user" />
                    </CInputGroupText>
                    <CFormInput
                      type="email"
                      v-model="username"
                      class="form-control"
                      id="username"
                      placeholder="Username"
                      autocomplete="username"
                    />
                  </CInputGroup>
                  <CInputGroup class="mb-4">
                    <CInputGroupText>
                      <CIcon icon="cil-lock-locked" />
                    </CInputGroupText>
                    <CFormInput
                      type="password"
                      v-model="password"
                      class="form-control"
                      id="floatingPassword"
                      placeholder="Password"
                      autocomplete="current-password"
                    />
                  </CInputGroup>
                  <!-- type="submit" -->
                  <CRow>
                    <CCol :xs="4">
                      <CButton color="primary" class="px-4" @click="submitForm"
                        >Login</CButton
                      >
                    </CCol>
                    <CCol :xs="8" class="text-right">
                      <CButton color="link" class="px-0 disabled ">
                        Forgot password?
                      </CButton>
                    </CCol>
                  </CRow>
                  <br /><br />
                  <CRow>
                    <hr />
                    <CCol :xs="12" class="d-grid gap-2 text-right">
                      <CButton color="dark" class="px-4" @click="demoLogin">
                        Demo User
                      </CButton>
                    </CCol>
                  </CRow>
                </CForm>
              </CCardBody>
            </CCard>
            <!-- <CCard class="text-white bg-primary py-5" style="width: 44%">
              <CCardBody class="text-center">
                <div>
                  <h2>Sign up</h2>
                  <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua.
                  </p>
                  <CButton
                    type="submit"
                    color="light"
                    variant="outline"
                    class="mt-3"
                  >
                    Register Now!
                  </CButton>
                </div>
              </CCardBody>
            </CCard> -->
          </CCardGroup>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  props: {
    msg: String,
  },
  data() {
    return {
      username: '',
      password: '',
      errors: [],
      token: '',
      apiURL: this.$store.state.apiURL,
    }
  },
  beforeMount() {
    // console.log('beforeMount')
    this.getCookie()
  },
  mounted() {
    document.title = 'Log In | BugFlix'
    // console.log('LOG:', document.title)
    // console.log('LOGin isAuthenticated:', this.$store.state.isAuthenticated)

    var togglePassword = document.getElementById('toggle-password')
    // var formContent = document.getElementsByClassName('form-content')[0]
    // var getFormContentHeight = formContent.clientHeight;

    // var formImage = document.getElementsByClassName('form-image')[0]
    // if (formImage) {
    //   var setFormImageHeight = (formImage.style.height =
    //     getFormContentHeight + 'px')
    // }
    if (togglePassword) {
      togglePassword.addEventListener('click', function () {
        var x = document.getElementById('password')
        if (x.type === 'password') {
          x.type = 'text'
        } else {
          x.type = 'password'
        }
      })
    }
  },
  methods: {
    getCookie() {
      if (document.cookie != '') {
        // When cookie is available then disable Login button
        // document.getElementById('login-btn').disabled = true;
        // console.log('loadCookie: ' + document.cookie)
        this.getCookieValue()
        return document.cookie
      } else {
        console.log('there is no cookie1')
      }
    },
    // Inject the cookie into token
    getCookieValue() {
      // cookieValue = document.cookie.split('; ').find((item) => item.startsWith('fastapiuser=')).split('=')[1];
      // console.log('cookieValue: ' + cookieValue);
      // token = cookieValue;
    },
    submitForm() {
      // console.log('test')
      // const form = event.currentTarget

      // form.preventDefault()
      // form.stopPropagation()

      const formData = new FormData()
      formData.append('username', this.username)
      formData.append('password', this.password)
      axios.post(`${this.apiURL}/login`, formData, {}).then((response) => {
        // console.log('LOGIN DATA: ', response)
        // handle success
        const token = response.data.access_token
        this.$store.commit('setToken', token)
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
        localStorage.setItem('token', token)
        const toPath = this.$route.query.to || '/theme/mydashboard'
        this.$router.push(toPath)
        // console.log('isAuthenticated: ', this.$store.state.isAuthenticated)
        this.$store.commit('setUsername', response.data.the_user.name)
        this.$store.commit('setUserID', response.data.the_user.id)
      })
    },
    demoLogin() {
      // console.log('Demo')
      const formData = new FormData()
      formData.append('username', 'demo@demo.com')
      formData.append('password', 'abc')
      axios.post(`${this.apiURL}/login`, formData, {}).then((response) => {
        // console.log('LOGIN DATA: ', response)
        // handle success
        const token = response.data.access_token
        this.$store.commit('setToken', token)
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
        localStorage.setItem('token', token)
        const toPath = this.$route.query.to || '/theme/projectlist'
        this.$router.push(toPath)
        // console.log('isAuthenticated: ', this.$store.state.isAuthenticated)
        this.$store.commit('setUsername', response.data.the_user.name)
        this.$store.commit('setUserID', response.data.the_user.id)
      })
    },
  },
}
</script>
