// Atlas AI low-risk qualification form placeholder.
// Do not add file upload fields for confidential/restricted materials.
// Final Wix Velo implementation must validate fields server-side and route Amber/Red cases to manual/secure review.
export function classifyLead(payload) {
  const sensitive = ['confidential', 'restricted'].includes(payload.dataProfile);
  const needsSecure = Boolean(payload.securePathNeed || sensitive || payload.hasCustomerFiles);
  return needsSecure ? 'architecture_review_required' : 'standard_qualification';
}
