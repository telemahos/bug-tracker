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
      <COffcanvasTitle>Offcanvas</COffcanvasTitle>
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
      Content for the offcanvas goes here. You can place just about any
      Bootstrap component or custom elements here.
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
}
</script>
