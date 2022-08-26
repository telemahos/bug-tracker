<template>
  <CButton
    color="primary"
    @click="
      () => {
        visibleEnd = !visibleEnd
      }
    "
    >Edit</CButton
  >
  <COffcanvas
    placement="end"
    :visible="visibleEnd"
    @hide="
      () => {
        visibleEnd = !visibleEnd
      }
    "
  >
    <COffcanvasHeader>
      <COffcanvasTitle>Offcanvas731</COffcanvasTitle>
      <CCloseButton
        class="text-reset"
        @click="
          () => {
            visibleEnd = false
          }
        "
      />
    </COffcanvasHeader>
    <COffcanvasBody>
      
      Kostas Nr:
      <CCol :xs="12">
        <CButton color="primary" type="submit">Submit Ticket</CButton>
        <div class="vr"></div>
        <CButton color="secondary" type="submit">Cancel </CButton>
      </CCol>
    </COffcanvasBody>
  </COffcanvas>
</template>
<script>
export default {
  data() {
    return {
      visibleEnd: false,
    }
  },
  props: ['foo'],
  created() {
    // props are exposed on `this`
    console.log(this.foo)
  }
}
</script>
