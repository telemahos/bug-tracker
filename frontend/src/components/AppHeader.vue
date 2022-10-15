<template>
  <CHeader position="sticky" class="mb-4">
    <CContainer fluid>
      <CHeaderToggler class="ps-1" @click="$store.commit('toggleSidebar')">
        <CIcon icon="cil-menu" size="lg" />
      </CHeaderToggler>
      <CHeaderBrand class="mx-auto d-lg-none" to="/">
        <!-- <CIcon :icon="logo" height="48" alt="Logo" /> -->
      </CHeaderBrand>
      <CHeaderNav
        class="d-none d-md-flex me-auto"
        v-if="this.$store.state.isAuthenticated"
      >
        <CNavItem>
          <!-- <CNavLink href="#/dashboard"> Dashboard </CNavLink> -->
          <CNavLink href="#/theme/mydashboard">My Dashboard </CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink href="#/theme/projectlist">Projects</CNavLink>
        </CNavItem>
        <CNavItem>
          <!-- <router-link to="/theme/ticket">Tickets</router-link> -->
          <CNavLink href="#/theme/ticketlist">Tickets</CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink href="#/theme/memberlist">Members</CNavLink>
        </CNavItem>
        <!-- <AppHeaderDropdownNew /> -->
      </CHeaderNav>
      <CHeaderNav>
        <CNavItem>
          <CNavLink v-if="this.$store.state.me" href="#/theme/mydashboard">
            <span class="text-muted">Hi,</span>
            {{ this.$store.state.me }}
          </CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink
            class="link-light"
            href="#/pages/Login"
            v-if="this.$store.state.isAuthenticated"
            ><small> Logout</small></CNavLink
          >
        </CNavItem>
        <CNavItem>
          <CNavLink
            class="link-info"
            href="#/pages/Login"
            v-if="!this.$store.state.isAuthenticated"
            >Login</CNavLink
          >
        </CNavItem>
      </CHeaderNav>
      <!-- <CHeaderNav>
         <CNavItem>
          <CNavLink href="#">
            <CIcon class="mx-2" icon="cil-bell" size="lg" />
          </CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink href="#">
            <CIcon class="mx-2" icon="cil-list" size="lg" />
          </CNavLink>
        </CNavItem>
        <CNavItem>
          <CNavLink href="#">
            <CIcon class="mx-2" icon="cil-envelope-open" size="lg" />
          </CNavLink>
        </CNavItem> <AppHeaderDropdownAccnt /> 
      </CHeaderNav>-->
    </CContainer>
    <CHeaderDivider />
    <CContainer fluid>
      <AppBreadcrumb />
    </CContainer>
  </CHeader>
</template>

<script>
import AppBreadcrumb from './AppBreadcrumb'
// import AppHeaderDropdownAccnt from './AppHeaderDropdownAccnt'
// import AppHeaderDropdownNew from './AppHeaderDropdownNew'
import { logo } from '@/assets/brand/logo'
// import Logout from '@/components/Logout'
export default {
  name: 'AppHeader',
  components: {
    AppBreadcrumb,
    // AppHeaderDropdownAccnt,
    // AppHeaderDropdownNew,
    // Logout,
  },
  setup() {
    return {
      logo,
    }
  },
}
</script>
