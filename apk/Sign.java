import com.android.apksig.*;import java.io.File;import java.security.*;import java.security.cert.*;import java.util.*;
public class Sign{public static void main(String[] a)throws Exception{
 KeyStore ks=KeyStore.getInstance("PKCS12");try(var in=new java.io.FileInputStream(a[0])){ks.load(in,"android".toCharArray());}
 PrivateKey k=(PrivateKey)ks.getKey("fu","android".toCharArray());X509Certificate c=(X509Certificate)ks.getCertificate("fu");
 ApkSigner.SignerConfig sc=new ApkSigner.SignerConfig.Builder("fu",k,List.of(c)).build();
 new ApkSigner.Builder(List.of(sc)).setInputApk(new File(a[1])).setOutputApk(new File(a[2])).setMinSdkVersion(24).setV1SigningEnabled(false).setV2SigningEnabled(true).build().sign();
 var r=new ApkVerifier.Builder(new File(a[2])).build().verify();System.out.println("verificado="+r.isVerified()+" v1="+r.isVerifiedUsingV1Scheme()+" v2="+r.isVerifiedUsingV2Scheme()+" erros="+r.getErrors());}}
