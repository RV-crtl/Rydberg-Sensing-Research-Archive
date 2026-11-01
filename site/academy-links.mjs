/** Safe source routing for educational Markdown rendered on site-only Pages. */
export const REPO="https://github.com/RV-crtl/Rydberg-Sensing-Research-Archive";
const BOOK_SOURCE=REPO+"/blob/main/book/chapters/";
const REPO_PREFIX=REPO+"/blob/main/";

export function resolveBookLink(input){
 if(typeof input!=="string"||!input.trim())throw new TypeError("Empty Markdown source link");
 if(/^https:\/\//i.test(input))return input;
 if(/^[a-z][\w+.-]*:/i.test(input)||input.startsWith("/")||input.includes("\\"))throw new TypeError("Blocked unsafe source URL");
 const resolved=new URL(input,BOOK_SOURCE);
 if(!resolved.href.startsWith(REPO_PREFIX))throw new TypeError("Link escaped the checked source repository");
 return resolved.href;
}
export function resolveBookAsset(path){
 if(typeof path!=="string")throw new TypeError("Invalid image reference");
 const match=path.match(/^\.\.\/\.\.\/site\/assets\/([A-Za-z0-9._-]+\.(?:svg|png|jpe?g|webp))$/i);
 if(!match)throw new TypeError("Only genuine checked site/assets images can be embedded in textbook");
 return "./assets/"+match[1];
}
