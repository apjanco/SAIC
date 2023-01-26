

select all hr, 
for hr in hrs 
for tag in soup.find_all("p"):
   print(tag)
   first two and last two are not what we want? 

<hr style='color:#8BB7C7' size='1' />


<p><span class='text-info'>IDENTIFICAÇÃO</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class='clsHitPesquisa'>ORIGEM</span>:&nbsp;L001&nbsp;DATA:&nbsp;20/02/86&nbsp;FORMUL:&nbsp;007&nbsp;DV:&nbsp;2&nbsp;TIPO:&nbsp;30&nbsp;&nbsp;31/10/86<br/><span class='text-info'>NOME</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Francisco&nbsp;das&nbsp;C.&nbsp;R.&nbsp;do&nbsp;Nascimento<br/><span class='text-info'>ENDEREÇO</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PÇ.&nbsp;DR&nbsp;Sebastião&nbsp;Martins&nbsp;307<br/><span class='text-info'>LOCALIZAÇÃO</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MUNICIPIO:&nbsp;NAZARE&nbsp;DO&nbsp;PIAUI&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UF:&nbsp;PI&nbsp;&nbsp;&nbsp;CEP:&nbsp;64802<br/><span class='text-info'>DADOS&nbsp;PESSOAIS</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SEXO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;01&nbsp;-&nbsp;MASCULINO<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MORADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;02&nbsp;-&nbsp;ZONA&nbsp;URBANA<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INSTRUÇÃO&nbsp;&nbsp;&nbsp;:&nbsp;02&nbsp;-&nbsp;PRIMEIRO&nbsp;GRAU&nbsp;INCOMPLETO<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ESTADO&nbsp;CIVIL:&nbsp;02&nbsp;-&nbsp;CASADO<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FAIXA&nbsp;ETÁRIA:&nbsp;05&nbsp;-&nbsp;30&nbsp;A&nbsp;39&nbsp;ANOS<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FAIXA&nbsp;RENDA&nbsp;:&nbsp;01&nbsp;-&nbsp;ATÉ&nbsp;1&nbsp;SALÁRIO&nbsp;MÍNIMO<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ATIVIDADE&nbsp;&nbsp;&nbsp;:&nbsp;05&nbsp;-&nbsp;COMÉRCIO&nbsp;DE&nbsp;MERCADORIAS<br/><span class='text-info'>DESTINATÁRIO</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JOÃO&nbsp;LOBO<br/><span class='text-info'>CATÁLOGO</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MANIFESTAÇÃO.<br/><span class='text-info'>INDEXAÇÃO</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MANIFESTAÇÃO&nbsp;DE&nbsp;APOIO.<br/><span class='text-info'>TEXTO</span><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sr.senador&nbsp;João&nbsp;Lobo,&nbsp;esperamos&nbsp;que&nbsp;a&nbsp;nova&nbsp;constituição&nbsp;seja&nbsp;mais<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fiel&nbsp;e&nbsp;defenda&nbsp;todos&nbsp;os&nbsp;cidadãos&nbsp;brasileiros.</p>

<hr style='color:#8BB7C7' size='1' />
