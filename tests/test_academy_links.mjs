import test from "node:test";
import assert from "node:assert/strict";
import {resolveBookLink,resolveBookAsset,REPO} from "../site/academy-links.mjs";
test("chapter reference correctly resolves to book (not repository root)",()=>{
 assert.equal(resolveBookLink("../REFERENCES.md"),REPO+"/blob/main/book/REFERENCES.md");
 assert.equal(resolveBookLink("../../docs/results/KEY_FINDINGS.md"),REPO+"/blob/main/docs/results/KEY_FINDINGS.md");
 assert.equal(resolveBookLink("02-operators-and-measurement.md"),REPO+"/blob/main/book/chapters/02-operators-and-measurement.md");
});
test("supports exact authored images and rejects outside resources",()=>{
 assert.equal(resolveBookAsset("../../site/assets/book-platform-selection.svg"),"./assets/book-platform-selection.svg");
 assert.throws(()=>resolveBookAsset("../../site/secret.md"),TypeError);
 assert.throws(()=>resolveBookAsset("javascript:alert(1)"),TypeError);
 assert.throws(()=>resolveBookLink("javascript:alert(1)"),TypeError);
 assert.throws(()=>resolveBookLink("../../../../other-repo/README.md"),TypeError);
});
